import telebot
from config import API_TOKEN
from telebot.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           Message)


keyboard = ReplyKeyboardMarkup()
button = KeyboardButton(text="FAAAAAAh")
button2 = KeyboardButton(text="дай-ка подумать...нет")

keyboard.add(button)
keyboard.add(button2)


bot = telebot.TeleBot(API_TOKEN)

state = 0

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    global state
    hello_message = f'Мы знакомы, <b>{message.from_user.username}</b>?'
    bot.send_message(
        message.chat.id,
        hello_message,
        reply_markup=keyboard,
        parse_mode='HTML' 

state = 1

  @bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    global state
    if message.text == "FAAAAAAh" and state == 1:
        bot.send_message(
            message.from_user.id,
            'Ну тогда давай сыграем в игру?',
        )
    elif message.text == "дай-ка подумать...нет" and state == 1:
        bot.send_message(
            message.from_user.id,
            'тогда надо познакомиться, меня зовут Роберт, давай поиграем?',
        )
      
    state = 2

  elif message.text == "давай" and state == 2:
        bot.send_message(
            message.from_user.id,
            'отлично, выбери в какую в дверь пойдешь:в левую или в правую?',
        )
  elif message.text == "давай" and state == 1:
        bot.send_message(
            message.from_user.id,
            'отлично, выбери в какую в дверь пойдешь:в левую или в правую?',
        )
    else:
        bot.send_message(
            message.from_user.id,
            'ты мне не нравишься...уходи'
        )



bot.infinity_polling()

