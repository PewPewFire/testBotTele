import telebot
import main
import time


bot = telebot.TeleBot(main.token) # в скобки токен

@bot.message_handler(commands=['start'])
def startMessage(msg):
    bot.send_photo(msg.from_user.id, photo= main.photo, reply_markup=buttons())

def buttons():  # Создали функцию для создания клавиатуры
    # markup = telebot.types.ReplyKeyboardMarkup(True)  # создали скелет для клавиатуры
    # btn1 = telebot.types.KeyboardButton('Button1')  # создали клавишу
    # btn2 = telebot.types.KeyboardButton('Button2')
    # btn3 = telebot.types.KeyboardButton('Button3')
    # markup.add(btn1, btn3)  # на скелет закинули клавишу
    # markup.add(btn2)
    # return markup  # вернули всю клавиатуру при вызове функции
    listAnswer = main.cityList
    markup = telebot.types.InlineKeyboardMarkup()
    for btn in listAnswer:
        button = telebot.types.InlineKeyboardButton(text=btn, callback_data=str(listAnswer.index(btn)))
    # btn1 = telebot.types.InlineKeyboardButton(text= "Ответ" ,callback_data= '1')
    # btn2 = telebot.types.InlineKeyboardButton(text = 'Ссылка',url='https://www.google.com/')
        markup.add(button)
    return markup
@bot.callback_query_handler(func=lambda call: True)
def callAnswer(call):
    # print(call)
    answer = main.cityQues
    if call.data == str(main.cityList.index(answer)):
        startMessage(call)
    else:
        print('Неправильно')
bot.infinity_polling()