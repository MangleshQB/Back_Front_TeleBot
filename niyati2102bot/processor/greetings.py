from django_tgbot.decorators import processor
from django_tgbot.exceptions import ProcessFailure
from django_tgbot.state_manager import update_types, state_types
from django_tgbot.types.replykeyboardremove import ReplyKeyboardRemove
from django_tgbot.types.update import Update
from ..bot import state_manager, TelegramBot
from ..models import TelegramState


state_manager.set_default_update_types(update_types.Message)


@processor(state_manager, from_states=state_types.All, success='asked_for_signin', fail=state_types.Keep)
def say_hello(bot: TelegramBot, update: Update, state: TelegramState):
    chat_id = update.get_chat().get_id()
    text = update.get_message().get_text().lower()
    try:
        username = update.get_message().get_user().username
    except:
        username = ''

    if "hello" in text:
        bot.sendMessage(chat_id, f'Hello {username} \nWelcome to QB shopping Bot.',  reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        photo_url = 'https://st2.depositphotos.com/3746151/10533/v/600/depositphotos_105336212-stock-illustration-hello-hand-lettering.jpg'
        bot.sendPhoto(chat_id, photo_url)
    elif "start" in text:
        bot.sendMessage(chat_id, f'Hello {username} \nWelcome to QB shopping Bot.', reply_markup=ReplyKeyboardRemove.a(remove_keyboard=True))
        photo_url = 'https://st2.depositphotos.com/3746151/10533/v/600/depositphotos_105336212-stock-illustration-hello-hand-lettering.jpg'
        bot.sendPhoto(chat_id, photo_url)

