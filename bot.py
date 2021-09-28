import telebot
import config
bot = telebot.TeleBot(config.2046245224:AAFnqiF1yAxTpV4Q1BpmVw-mD3ubrYXrL64)
@bot.message_handler(content_types=['text'])
def lalala(message):
    
 bot.send_message(message.chat.id, message.text)
#RUN
bot.polling(none_stop=True)
