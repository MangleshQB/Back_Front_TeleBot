from django_tgbot.decorators import processor
from django_tgbot.exceptions import ProcessFailure
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardremove import ReplyKeyboardRemove
from .bot import state_manager, TelegramBot
from .models import TelegramState
import requests

state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states=state_types.All, success='start')
def hello_world(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text().lower()
    username = update.get_message().get_user().username
    print(text, update.get_message().get_user().username)
    if "start" in text:
        bot.sendMessage(chat_id, f'Hello {username}, How are you?')
        state.set_name('start')
    elif "good morning" in text:
        bot.sendMessage(chat_id, f'Good Morning, {username}')


@processor(state_manager, success='asked_for_signup', from_states='start')
def say_hello(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    bot.sendMessage(chat_id, 'Hello! and welcome to QB shopping bot :)')
    bot.sendMessage(chat_id, 'Have you signed up yet?', reply_markup=ReplyKeyboardMarkup.a(keyboard=[
        [KeyboardButton.a(text='Yes'), KeyboardButton.a(text='Do it now')]
    ]))


@processor(state_manager, from_states='asked_for_signup', success=state_types.Keep, exclude_message_types=message_types.Text)
def text_only(bot, update, state):
    bot.sendMessage(update.get_chat().get_id(), 'I\'d appreciate it if you answer in text format 😅')


@processor(state_manager, from_states='asked_for_signup', message_types=message_types.Text  )
def start_signup(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text()
    if text == 'Yes!':
        bot.sendMessage(chat_id, 'Amazing!', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('')
    elif text == 'Do it now!':
        bot.sendMessage(chat_id, 'Oh absolutely! Let\'s start with your Email:', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('asked_for_email')
    else:
        bot.sendMessage(chat_id, 'I didn\'t get that! Use the keyboard below')


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

    email = state.get_memory()['email']
    bot.sendMessage(chat_id, 'Thanks! You successfully signed up with these details:\nEmail: {}\nPassword: {}'.format(email, password))

    # Login api call
    data = {'email': email,
            'password': password,
            }

    r = requests.post(url='http://192.168.5.106:8000/login/', data=data)
    if r.status_code == 200:
        bot.sendMessage(chat_id, 'Thanks! You successfully signed up with these details:\nEmail: {}\nPassword: {}'.format(email, password))
    else:
        bot.sendMessage(chat_id, 'No active account found for this credentials:\nEmail: {}\nPassword: {}'.format(email, password))