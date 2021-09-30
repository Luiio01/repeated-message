import telebot
import config
from apscheduler.schedulers.background import BackgroundScheduler



app = Client("my_account")


def job():
    app.send_message("me", "Hi!")


scheduler = BackgroundScheduler()
scheduler.add_job(job, "interval", seconds=3)

scheduler.start()
app.run()

bot = telebot.TeleBot(config. TOKEN)
@bot.message_handler(content_types=['text'])
def lalala(message):
    
 bot.send_message(message.chat.id, message.text)
#RUN
bot.polling(none_stop=True)
