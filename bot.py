import time
import schedule
import requests


def telegram_bot_sendtext(bot_message):
    
    bot_token = '2046245224:AAFnqiF1yAxTpV4Q1BpmVw-mD3ubrYXrL64'
    bot_chatID = '2046245224'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
 my_message = "sono io il primo ".   ## Customize your message
    telegram_bot_sendtext(my_message)


    
schedule.every().day.at("19:00").do(report)

while True:
    schedule.run_pending()
    time.sleep(1)
