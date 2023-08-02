import requests
from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from django_tgbot.exceptions import ProcessFailure
from ..bot import state_manager, TelegramBot
from ..models import TelegramState
from django_tgbot.types.replykeyboardremove import ReplyKeyboardRemove

state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states='asked_for_signup', message_types=message_types.Text, fail=state_types.Keep)
def start_signup(bot, update, state):
    chat_id = update.get_chat().get_id()
    bot.sendMessage(chat_id, 'Enter your email address', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
    state.set_name('asked_for_signup_email')


@processor(state_manager, from_states='asked_for_signup_email', success='asked_for_firstname', fail=state_types.Keep, message_types=message_types.Text)
def get_signup_email(bot, update, state):
    chat_id = update.get_chat().get_id()
    email = update.get_message().get_text()

    if email.find('@') == -1:
        bot.sendMessage(chat_id, 'Invalid email address! Send again:')
        raise ProcessFailure

    state.set_memory({
        'email': email
    })

    bot.sendMessage(chat_id, 'Firstname:')


@processor(state_manager, from_states='asked_for_firstname', fail=state_types.Keep, message_types=message_types.Text, success='asked_for_lastname')
def get_firstname(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    firstname = update.get_message().get_text()

    try:
        email = state.get_memory()['email']
    except:
        email = ''
    state.set_memory({
        'email': email,
        'firstname': firstname
    })

    bot.sendMessage(chat_id, 'Lastname:')


@processor(state_manager, from_states='asked_for_lastname', fail=state_types.Keep, message_types=message_types.Text, success='asked_for_address')
def get_lastname(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    address = update.get_message().get_text()

    try:
        email = state.get_memory()['email']
    except:
        email = ''

    try:
        firstname = state.get_memory()['firstname']
    except:
        firstname = ''

    try:
        lastname = state.get_memory()['firstname']
    except:
        lastname = ''

    state.set_memory({
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'address': address,
    })

    bot.sendMessage(chat_id, 'City:')


@processor(state_manager, from_states='asked_for_address', fail=state_types.Keep, message_types=message_types.Text, success='asked_for_city')
def get_lastname(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    city = update.get_message().get_text()

    try:
        email = state.get_memory()['email']
    except:
        email = ''

    try:
        firstname = state.get_memory()['firstname']
    except:
        firstname = ''

    try:
        lastname = state.get_memory()['firstname']
    except:
        lastname = ''

    try:
        address = state.get_memory()['firstname']
    except:
        address = ''

    state.set_memory({
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'address': address,
        'city': city,
    })

    bot.sendMessage(chat_id, 'State:')


@processor(state_manager, from_states='asked_for_city', fail=state_types.Keep, message_types=message_types.Text, success='asked_for_state')
def get_lastname(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    state = update.get_message().get_text()


    try:
        email = state.get_memory()['email']
    except:
        email = ''

    try:
        firstname = state.get_memory()['firstname']
    except:
        firstname = ''

    try:
        lastname = state.get_memory()['firstname']
    except:
        lastname = ''

    try:
        address = state.get_memory()['firstname']
    except:
        address = ''

    try:
        city = state.get_memory()['firstname']
    except:
        city = ''

    state.set_memory({
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'address': address,
        'city': city,
        'state': state,
    })

    bot.sendMessage(chat_id, 'Country:')


@processor(state_manager, from_states='asked_for_state', fail=state_types.Keep, message_types=message_types.Text, success='asked_for_country')
def get_lastname(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    country = update.get_message().get_text()

    try:
        email = state.get_memory()['email']
    except:
        email = ''

    try:
        firstname = state.get_memory()['firstname']
    except:
        firstname = ''

    try:
        lastname = state.get_memory()['firstname']
    except:
        lastname = ''

    try:
        address = state.get_memory()['firstname']
    except:
        address = ''

    try:
        city = state.get_memory()['firstname']
    except:
        city = ''

    try:
        state = state.get_memory()['firstname']
    except:
        state = ''

    state.set_memory({
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'address': address,
        'city': city,
        'state': state,
        'country': country,
    })

    bot.sendMessage(chat_id, 'pincode:')


@processor(state_manager, from_states='asked_for_country', fail=state_types.Keep, message_types=message_types.Text, success='asked_for_pincode')
def get_lastname(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    pincode = update.get_message().get_text()

    try:
        email = state.get_memory()['email']
    except:
        email = ''

    try:
        firstname = state.get_memory()['firstname']
    except:
        firstname = ''

    try:
        lastname = state.get_memory()['firstname']
    except:
        lastname = ''

    try:
        address = state.get_memory()['firstname']
    except:
        address = ''

    try:
        city = state.get_memory()['firstname']
    except:
        city = ''

    try:
        state = state.get_memory()['firstname']
    except:
        state = ''

    try:
        country = state.get_memory()['firstname']
    except:
        country = ''

    state.set_memory({
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'address': address,
        'city': city,
        'state': state,
        'country': country,
        'pincode': pincode,
    })

    bot.sendMessage(chat_id, 'Phone Number:')


@processor(state_manager, from_states='asked_for_pincode', fail=state_types.Keep, message_types=message_types.Text, success='asked_for_signup_password')
def get_lastname(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    phone_number = update.get_message().get_text()

    try:
        email = state.get_memory()['email']
    except:
        email = ''

    try:
        firstname = state.get_memory()['firstname']
    except:
        firstname = ''

    try:
        lastname = state.get_memory()['firstname']
    except:
        lastname = ''

    try:
        address = state.get_memory()['firstname']
    except:
        address = ''

    try:
        city = state.get_memory()['firstname']
    except:
        city = ''

    try:
        state = state.get_memory()['firstname']
    except:
        state = ''

    try:
        country = state.get_memory()['firstname']
    except:
        country = ''

    try:
        pincode = state.get_memory()['firstname']
    except:
        pincode = ''

    state.set_memory({
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'address': address,
        'city': city,
        'state': state,
        'country': country,
        'pincode': pincode,
        'phone_number': phone_number,
    })

    bot.sendMessage(chat_id, 'Password:')


@processor(state_manager, from_states='asked_for_signup_password', fail=state_types.Keep, message_types=message_types.Text)
def get_signup_password(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    password = update.get_message().get_text()
    if len(password) < 3:
        bot.sendMessage(chat_id, 'Password is too short! Try again:')
        raise ProcessFailure

    try:
        email = state.get_memory()['email']
    except:
        email = ''

    try:
        firstname = state.get_memory()['firstname']
    except:
        firstname = ''

    try:
        lastname = state.get_memory()['firstname']
    except:
        lastname = ''

    try:
        address = state.get_memory()['firstname']
    except:
        address = ''

    try:
        city = state.get_memory()['firstname']
    except:
        city = ''

    try:
        state = state.get_memory()['firstname']
    except:
        state = ''

    try:
        country = state.get_memory()['firstname']
    except:
        country = ''

    try:
        pincode = state.get_memory()['firstname']
    except:
        pincode = ''

    try:
        phone_number = state.get_memory()['firstname']
    except:
        phone_number = ''

    data = {
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'address': address,
        'city': city,
        'state': state,
        'country': country,
        'pincode': pincode,
        'phone_number': phone_number,
        'password': password,
    }

    print("Data == ", data)

    r = requests.post(url='http://192.168.5.106:8000/signup/', data=data)
    if r.status_code == 201:
        bot.sendMessage(chat_id, 'Thanks! You successfully signed up with these details:\nEmail: {}\nPassword: {}, \nFirstname: {}, \nLastname: {}'.format(email, password, firstname, lastname))
        bot.sendMessage(chat_id, 'Now login to your account.')
        state.set_name('asked_for_signin')
    else:
        # bot.sendMessage(chat_id, f'Error -> {r.reason}')
        bot.sendMessage(chat_id, 'User already exists.')
        bot.sendMessage(chat_id, 'Sign up again')
        state.set_name('asked_for_signup')

