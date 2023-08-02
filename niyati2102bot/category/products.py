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


@processor(state_manager, from_states='products', message_types=message_types.Text, fail='products', success=state_types.Reset)
def start_products(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text().lower()

    bot.sendMessage(chat_id, f'These are the options you have in {text}.', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
    print(text)

    r = requests.get(url=f'http://192.168.5.106:8000/product/?name={text}')
    print(r.text)

    if r.status_code == 200:
        categories = json.loads(r.text)

        if type(categories["Products"]) == str:
            bot.sendMessage(chat_id, 'Wrong Option Try again.')
            raise ProcessFailure

        for data in categories["Products"]:
            imgUrl = "https://8bc8-2405-201-2002-1f6-2042-3118-5338-76fc.ngrok-free.app/" + data["product_image"]
            message = f'Name: {data["name"]} \nDescription: {data["description"]} \nPrice : {data["price"]}'
            bot.sendPhoto(chat_id, imgUrl, caption=message)

            bot.sendMessage(chat_id, 'Want to add any product to cart?', reply_markup=ReplyKeyboardMarkup.a(keyboard=[
                [KeyboardButton.a(text='Yes'), KeyboardButton.a(text='Go to cart'), KeyboardButton.a(text='Continue exploring'), KeyboardButton.a(text='No')]]))

    else:
        bot.sendMessage(chat_id, 'Try again.')
        state.set_name('products')


@processor(state_manager, from_states='further_products', message_types=message_types.Text, fail='products')
def start_products(bot, update, state):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text().lower()

    if text == 'yes':
        bot.sendMessage(chat_id, "Enter product name", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('add_to_cart')

    elif text == 'no':
        bot.sendMessage(chat_id, "Have a good day.", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('logout')

    elif text == 'go to cart':
        bot.sendMessage(chat_id, "We are showing your cart.", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('go to cart')

    elif text == 'continue exploring':
        bot.sendMessage(chat_id, "Let\'s find other products", reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        state.set_name('products')