import telebot
import time

dictionary_of_links = {
    1: "google.com",
    2: "amin.ir",
    3: "ghasem.net",
    4: "asheghy"
}
# اسم سایتا عالی :)

bot = telebot.TeleBot("895692273:AAGmqn6xVZShiS1l9vNXNcrf83iXRnL8BVk")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام.\n به مسابقه‌ی جشن نیمه شعبان خوش آمدید.")
    send_help(message)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "با زدن دستور /number شماره مورد نظر خود را به ما بفرستید تا ما لینک وویس را در اختیارتان "
                          "قرار دهیم.\n همچنین می‌توانید با زدن دستور /about اطلاعات بات را مشاهده کنید.")


@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "این بات به عشق ظهور آقا ساخته شده است.")


@bot.message_handler(commands=['number'])
def send_number_message(message1):
    bot.reply_to(message1, "لطفا عدد مورد نظر خود را وارد نمایید.")

    @bot.message_handler(func=lambda message: True)
    def send_voice_link(message2):
        # check if file exists
        if int(message2.text) in dictionary_of_links:
            response_message = "https://path/to/source/" + message2.text + ".mp3"
        else:
            response_message = "شماره مورد نظر یافت نشد!"
        bot.reply_to(message2, response_message)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(6)
