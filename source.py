import telebot
import time

dictionary_of_links = {
    1 : "google.com",
    2 : "ghasem.ir",
    3 : "amin.ir",
    4 : "ashegh sho.del",
    5 : "koooft"
}
bot = telebot.TeleBot("895692273:AAGmqn6xVZShiS1l9vNXNcrf83iXRnL8BVk")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام.\n به مسابقه‌ی جشن نیمه شعبان خوش آمدید.")
    send_help(message)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "با زدن /number شماره مورد نظر خود را به ما بفرستید تا ما لینک وویس را در اختیارتان قرار "
                          "دهیم.")


@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "این بات به عشق ظهور آقا ساخته شده است.")


@bot.message_handler(commands=['number'])
def send_number_message(message1):
    bot.reply_to(message1, "لطفا عدد مورد نظر خود را وارد نمایید.")

    @bot.message_handler(func=lambda message: True)
    def send_voice_link(message2):
        bot.reply_to(message2, "https://path/to/source/" + message2.text + ".mp3")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(6)
