import telebot

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

bot.polling();