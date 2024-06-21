from telebot import types

from datac.loader import bot
from datac.text import *


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_1')
def step_1(call):
    _chat_id = call.message.chat.id
    _photo = open('res/img/img_1.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тык <', callback_data='call_step_2')
    )
    bot.send_photo(_chat_id, photo=_photo, caption=t_step_1, reply_markup=_markup, parse_mode='html')
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_2')
def step_2(call):
    _chat_id = call.message.chat.id
    _photo = open('res/img/img_22.jpg', 'rb')
    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тап <', callback_data='call_step_3')
    )

    bot.send_photo(_chat_id, photo=_photo, caption=t_step_2, reply_markup=_markup, parse_mode='html')
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_3')
def step_3(call):
    _chat_id = call.message.chat.id
    _photo1 = open('res/img/img_31.jpg', 'rb')
    _photo2 = open('res/img/img_32.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тук <', callback_data='call_step_4')
    )
    bot.send_photo(_chat_id, photo=_photo1)
    bot.send_photo(_chat_id, photo=_photo2)
    bot.send_message(_chat_id, t_step_3, reply_markup=_markup)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_4')
def step_4(call):
    _chat_id = call.message.chat.id
    _photo = open('res/img/img_99.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Продолжим <', callback_data='call_step_5')
    )
    bot.send_photo(_chat_id, photo=_photo, caption=t_step_4, reply_markup=_markup, parse_mode='html')
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_5')
def step_5(call):
    _chat_id = call.message.chat.id
    _photo1 = open('res/img/img_31.jpg', 'rb')
    _photo2 = open('res/img/img_32.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тук <', callback_data='call_step_6')
    )
    bot.send_photo(_chat_id, photo=_photo1)
    bot.send_photo(_chat_id, photo=_photo2)
    bot.send_message(_chat_id, t_step_3, reply_markup=_markup)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_6')
def step_6(call):
    _chat_id = call.message.chat.id
    _photo1 = open('res/img/img_41.jpg', 'rb')
    _photo2 = open('res/img/img_42.jpg', 'rb')
    _photo3 = open('res/img/img_43.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тык <', callback_data='call_step_7')
    )
    bot.send_photo(_chat_id, photo=_photo1)
    bot.send_photo(_chat_id, photo=_photo2)
    bot.send_photo(_chat_id, photo=_photo3)
    bot.send_message(_chat_id, t_step_5, reply_markup=_markup)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_7')
def step_7(call):
    _chat_id = call.message.chat.id

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> КАКОЙ ГУСЬ?! <', callback_data='call_step_guse')
    )
    bot.send_message(_chat_id, t_step_6, reply_markup=_markup)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_guse')
def step_guse(call):
    _chat_id = call.message.chat.id
    _photo1 = open('res/img/img_51.jpg', 'rb')
    _photo2 = open('res/img/img_52.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> тык тык ТЫК <', callback_data='call_step_8')
    )
    bot.send_photo(_chat_id, photo=_photo2)
    bot.send_photo(_chat_id, photo=_photo1)
    bot.send_message(_chat_id, 'Большой и классный с порванной... кхем.. кхем... давай "тык" дальше', reply_markup=_markup)
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_8')
def step_8(call):
    _chat_id = call.message.chat.id
    _photo = open('res/img/img_6.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тык <', callback_data='call_step_9')
    )

    bot.send_photo(_chat_id, photo=_photo, caption=t_step_7, reply_markup=_markup, parse_mode='html')
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_9')
def step_9(call):
    _chat_id = call.message.chat.id
    _photo = open('res/img/img_7.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тык <', callback_data='call_step_10')
    )

    bot.send_photo(_chat_id, photo=_photo, caption=t_step_8, reply_markup=_markup, parse_mode='html')
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_10')
def step_10(call):
    _chat_id = call.message.chat.id
    _photo = open('res/img/img_8.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тык Тык Тык...... Тыыыыык <', callback_data='call_step_11')
    )

    bot.send_photo(_chat_id, photo=_photo, caption=t_step_9, reply_markup=_markup, parse_mode='html')
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_11')
def step_11(call):
    _chat_id = call.message.chat.id
    _photo = open('res/img/img_9.jpg', 'rb')

    _markup = types.InlineKeyboardMarkup()
    _markup.add(
        types.InlineKeyboardButton('> Тап <', callback_data='call_step_12')
    )

    bot.send_photo(_chat_id, photo=_photo, caption=t_step_10, reply_markup=_markup, parse_mode='html')
    bot.answer_callback_query(call.id, text="")


@bot.callback_query_handler(func=lambda call: call.data == 'call_step_12')
def step_12(call):
    _chat_id = call.message.chat.id

    bot.send_message(_chat_id, t_congratulation)
    bot.answer_callback_query(call.id, text="")
