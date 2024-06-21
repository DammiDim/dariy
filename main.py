from datac.loader import bot

from handlers import handler_com, handler_call


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=1)

