from telebot import types

from datac.loader import bot
from datac.text import *


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.clear_reply_handlers(message)

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('Поехали', callback_data='call_step_1')
    )

    bot.send_message(message.chat.id, t_welcome, reply_markup=_markup)
