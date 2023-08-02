import json
import requests
from django_tgbot.decorators import processor
from django_tgbot.exceptions import ProcessFailure
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.keyboardbutton import KeyboardButton
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup

from ..bot import state_manager
from django_tgbot.types.replykeyboardremove import ReplyKeyboardRemove

state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states='select_categories', message_types=message_types.Text, fail=state_types.Keep, success='products')
def start_categories(bot, update, state):

    chat_id = update.get_chat().get_id()
    bot.sendMessage(chat_id, 'Amazing!', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
    bot.sendMessage(chat_id, 'Let\'s see the options you have.', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))

    r = requests.get(url='http://192.168.5.106:8000/categorylist/')

    if r.status_code == 200:

        categories = json.loads(r.text)

        for data in categories:
            data = f'{data["id"]}. {data["name"]}'
            bot.sendMessage(chat_id, data)

        bot.sendMessage(chat_id, 'Which category are you interested in?', reply_markup=ReplyKeyboardMarkup.a(keyboard=[[KeyboardButton.a(text='Jeans'), KeyboardButton.a(text='Tshirt'), KeyboardButton.a(text='Shirt'), KeyboardButton.a(text='Top'), KeyboardButton.a(text='Shorts')]]))
        state.set_name('products')
    else:
        bot.sendMessage(chat_id, 'Try again.')
        raise ProcessFailure
