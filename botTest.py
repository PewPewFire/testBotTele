import telebot
import main


bot = telebot.TeleBot(main.token)

@bot.message_handler(content_types=['photo'])
def photoSend(msg):
    print(msg)




bot.infinity_polling()