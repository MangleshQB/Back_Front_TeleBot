import requests
from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.update import Update
from django_tgbot.exceptions import ProcessFailure
from ..bot import state_manager, TelegramBot
from ..models import TelegramState
from django_tgbot.types.replykeyboardremove import ReplyKeyboardRemove

state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states='asked_for_signin', message_types=message_types.Text, fail=state_types.Keep)
def start_signin(bot, update, state):
    chat_id = update.get_chat().get_id()

    bot.sendMessage(chat_id, 'Do you have an account?', reply_markup=ReplyKeyboardMarkup.a(keyboard=[[KeyboardButton.a(text='Yes'), KeyboardButton.a(text='No')]]))
    state.set_name('asked_for_signin_ans')


@processor(state_manager, from_states='asked_for_signin_ans', message_types=message_types.Text, fail=state_types.Keep)
def asked_for_signin_ans(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text().lower()
    print(text)

    if text == 'yes':
        bot.sendMessage(chat_id, 'Amazing!', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        bot.sendMessage(chat_id, 'Enter your registered email address', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('asked_for_email')
    elif text == 'no':
        bot.sendMessage(chat_id, "Let's create one then", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        bot.sendMessage(chat_id, "Type anything to create one.", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('asked_for_signup')


@processor(state_manager, from_states='asked_for_email', success='asked_for_password', fail=state_types.Keep, message_types=message_types.Text)
def get_email(bot, update, state):
    chat_id = update.get_chat().get_id()
    email = update.get_message().get_text()

    if email.find('@') == -1:
        bot.sendMessage(chat_id, 'Invalid email address! Send again:')
        raise ProcessFailure

    state.set_memory({
        'email': email
    })

    bot.sendMessage(chat_id, 'Beautiful! What is your password?')


@processor(state_manager, from_states='asked_for_password', fail=state_types.Keep, message_types=message_types.Text)
def get_password(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    password = update.get_message().get_text()
    if len(password) < 3:
        bot.sendMessage(chat_id, 'Password is too short! Try again:')
        raise ProcessFailure

    try:
        email = state.get_memory()['email']
    except:
        email = ""

    data = {'email': email,
            'password': password
            }

    r = requests.post(url='http://192.168.5.106:8000/login/', data=data)
    if r.status_code == 200:
        bot.sendMessage(chat_id, 'Thanks! You successfully signed in with these details:\nEmail: {}\nPassword: {}'.format(email, password))
        bot.sendMessage(chat_id, 'Do you wanna see the categories?', reply_markup=ReplyKeyboardMarkup.a(keyboard=[[KeyboardButton.a(text='Yes'), KeyboardButton.a(text='No')]]))
        state.set_name('asked_for_password_ans')

    elif r.status_code != 200:
        bot.sendMessage(chat_id, 'No active account found for this credentials:\nEmail: {}\nPassword: {}'.format(email, password))
        bot.sendMessage(chat_id, 'Create an account')
        bot.sendMessage(chat_id, "Type anything to create one.", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('asked_for_signup')

    else:
        bot.sendMessage(chat_id, 'Do you have an account?', reply_markup=ReplyKeyboardMarkup.a(keyboard=[[KeyboardButton.a(text='Yes'), KeyboardButton.a(text='No')]]))
        raise ProcessFailure


@processor(state_manager, from_states='asked_for_password_ans', message_types=message_types.Text, fail=state_types.Reset, success="select_categories")
def asked_for_password_ans(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text().lower()
    print(text)

    if text == 'yes':
        bot.sendMessage(chat_id, 'Cool')
        bot.sendMessage(chat_id, 'Type anything to see the categories')
        state.set_name('select_categories')

    elif text == 'No':
        bot.sendMessage(chat_id, 'See you later then.')
        raise ProcessFailure