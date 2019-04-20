import telebot
import time

dictionary_of_links = {
    10110: "https://drive.google.com/file/d/1tuq7q5QzeHZiF4O1FRvMjdRG6MgeXoIH/view?usp=sharing",
    20110: "https://drive.google.com/file/d/1uhqzCFDW7EJDbFtvrXVsm7mnKjWzzZdY/view?usp=sharing",
    20210: "https://drive.google.com/file/d/1arFOwTHL77FXftP5Ab3mduXLSKFGlXx8/view?usp=sharing",
    30110: "https://drive.google.com/file/d/1rsFADUqFVdG5hwVWe-xBFdcg778dxuKf/view?usp=sharing",
    30210: "https://drive.google.com/file/d/1H3UxHnZOWTLp4SBKTx96G40uF9DSnxdY/view?usp=sharing",
    30310: "https://drive.google.com/file/d/1b1v4JQQ74pQrOf0EmQlqcyNvGEwvGEzK/view?usp=sharing",
    30410: "https://drive.google.com/file/d/1pMf6aUe_qLxg1lecCLuchPgpLXHFSTLu/view?usp=sharing",
    30510: "https://drive.google.com/file/d/1aK2QV7FgfGiR5WhOa_nqCMepGy-ZYSUv/view?usp=sharing",
    30610: "https://drive.google.com/file/d/1Yx9O029zXaOb_1jIPlg67tpsIwSBV0Li/view?usp=sharing",
    40110: "https://drive.google.com/file/d/1k3CIHZDXqv5a78Z0ScMg9j3JoDfdBoqW/view?usp=sharing",
    40210: "https://drive.google.com/file/d/1n49g9_d9Dm7URXKjDMpulJOaZiZL5jRy/view?usp=sharing",
    40310: "https://drive.google.com/file/d/1Eq_itjza4M4suy7F8O_qE1d_54bwYq5i/view?usp=sharing",
    40410: "https://drive.google.com/file/d/1zdqPB0RDt0s1x6xiYhzuFv44Z3KU9yfG/view?usp=sharing",
    40510: "https://drive.google.com/file/d/1o1go28ifg5nUsnkHm-YaTIHN196K314W/view?usp=sharing",
    40610: "https://drive.google.com/file/d/1bqhIZeIfGwUC_RxnkJtwvJn_hCWJzIwC/view?usp=sharing",
    50110: "https://drive.google.com/file/d/14Q4gw0UmqSlCGpvckpj8eklmwcmSHkDW/view?usp=sharing",
    50210: "https://drive.google.com/file/d/12R6vzltwunqw0SIbe6f_ofmssuTxniPp/view?usp=sharing",
    50310: "https://drive.google.com/file/d/1b_N8N3oDnoIQeNT73YWuv6J_GFmtn-14/view?usp=sharing",
    70110: "https://drive.google.com/file/d/1xHCvKYmnoLcbk8pqL7qJkIfHTfYr39re/view?usp=sharing",
    80110: "https://drive.google.com/file/d/12Yv7CzFPloQ33toZpjZZN2mvMKAUyIZq/view?usp=sharing"
}

bot = telebot.TeleBot("895692273:AAGmqn6xVZShiS1l9vNXNcrf83iXRnL8BVk")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    send_help(message)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "با زدن دستور /number شماره مورد نظر خود را به ما بفرستید تا ما لینک وویس را در اختیارتان "
                          "قرار دهیم.")


@bot.message_handler(commands=['number'])
def send_number_message(message1):
    bot.reply_to(message1, "لطفا عدد مورد نظر خود را وارد نمایید.")

    @bot.message_handler(func=lambda message: True)
    def send_voice_link(message2):
        # check if file exists
        if int(message2.text) in dictionary_of_links:
            response_message = dictionary_of_links[int(message2.text)]
        else:
            response_message = "شماره مورد نظر یافت نشد!"
        bot.reply_to(message2, response_message)


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(6)
