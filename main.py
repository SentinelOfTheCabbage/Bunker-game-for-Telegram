from telebot    import TeleBot, types
from settings   import TOKEN
from time       import sleep
# from controller import Controller
from updater    import Update
bot = TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    message = Update(message=message)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        text='button', callback_data='callback'))
    bot.send_message(message.user_id, 'MESSAGE', reply_markup=markup)


@bot.callback_query_handler(func=lambda message: True)
def handle_callbacks(callback):
    callback = Update(callback=callback)

if __name__ == '__main__':
    while True:
        try:
            print('STARTING')
            bot.polling(none_stop=True)
        except:
            bot.stop_polling()
            sleep(15)
            print('Falling =(')
            continue
