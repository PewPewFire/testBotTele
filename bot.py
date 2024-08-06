import telebot
import main
import time


bot = telebot.TeleBot(main.token) # в скобки токен

@bot.message_handler(commands=['start', "help", "info"])
def firstmessage(message):
    print(message)
    if message.text == '/start':
        bot.send_message(chat_id=message.from_user.id, text='Привет!'
                                                             'Для ознакомления напишите /info')
    elif message.text == "/help":
        bot.send_message(chat_id=message.from_user.id, text = "Пока помочь не могу. ")
    elif message.text == "/info":
        bot.send_message(chat_id=message.from_user.id, text = f"Здравствуйте {message.from_user.first_name}, бот имеет несколько команд такие как: /star, /help и /info")

@bot.message_handler(content_types=["text"])
def textMessage(message):
    print(message.text.lower())
   # if message.text.lower() == "привет":
     #   bot.send_message(chat_id=message.from_user.id, text= 'Привет!')
    if message.text.lower() in "привет":
        bot.send_message(chat_id=message.from_user.id, text= "Привет! ")

@bot.message_handler(content_types=['photo'])
def photoMessage(message):
    print(message.photo[0])
    print(message.photo[1])
    print(message.photo[2])


@bot.message_handler(content_types=['dice'])
def messageDice(msg):
    print(msg)

    # msgBot = bot.send_dice(msg.from_user.id)
    # userScore = msg.dice.value
    # botScore = msgBot.dice.value
    # time.sleep(3)
    # if botScore > userScore:
    #     bot.send_message(msg.from_user.id, text= "Ты приограл!")
    # elif botScore < userScore:
    #     bot.send_message(msg.from_user.id, text="Ты выиграл!")
    # else:
    #     bot.send_message(msg.from_user.id, text="Ничья!")
    ballBot = bot.send_dice(msg.from_user.id, emoji= '⚽')
    botcore = int(ballBot.dice.value > 2)
    userHit = int(msg.dice.value > 2)
    scoreUser = 0
    scoreBot = 0
    scoreBot += botcore
    scoreUser += userHit
    time.sleep(3)
    bot.send_message(msg.from_user.id, text = f'Игрок: {scoreUser}, Бот {scoreBot}')


# 1 и 2 - мимо
# остальное - попал
bot.infinity_polling()