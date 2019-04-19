import telebot
import time


bot = telebot.TeleBot("895692273:AAGmqn6xVZShiS1l9vNXNcrf83iXRnL8BVk")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "اینجا پیام شروع خواهد بود")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "اینجا پیام کمک خواهد بود")


@bot.message_handler(commands=['about'])
def send_help(message):
    bot.reply_to(message, "اینجا پیام معرفی خواهد بود")

@bot.message_handler(commands=['number'])
def send_number_message(message1):
    bot.reply_to(message1, "عدد مورد نظر خود را وارد بنما")
    @bot.message_handler(func=lambda message: True)
    def send_voice_link(message2):
        bot.reply_to(message2, "link number " + message2.text)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(6)

