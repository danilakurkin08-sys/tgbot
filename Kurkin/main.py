import telebot
from telebot.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           Message)

API_TOKEN ='8576595076:AAGywQ3XFGagq1Cqben1PoLtQZC1L6RqVoA'

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

keyboard = ReplyKeyboardMarkup()
button = KeyboardButton(text="да")
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
    )
state = 1

@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    global state
    if message.text == "да" and state == 1:
        
        bot.send_message(
            message.from_user.id,
            'Ну тогда давай сыграем в игру?',
            reply_markup=ReplyKeyboardMarkup().add("ну давай","не хочу" )
        )

        state = 2

    elif message.text == "дай-ка подумать...нет" and state == 1:
        bot.send_message(
            message.from_user.id,
            'Тогда надо познакомиться, меня зовут Роберт, давай поиграем?',
             reply_markup=ReplyKeyboardMarkup().add("ну давай","не хочу" )
        )

    elif message.text == "ну давай" and state == 2:
        bot.send_message(
            message.from_user.id,
            'Отлично, выбери в какую в дверь пойдешь:в левую или в правую?',
            reply_markup=ReplyKeyboardMarkup().add("левая","правая")
        )
            
    elif message.text == "ну давай" and state == 2:
        bot.send_message(
            message.from_user.id,
            'Отлично, выбери в какую в дверь пойдешь:в левую или в правую?',
            reply_markup=ReplyKeyboardMarkup().add("левая","правая")
        )
        state = 3

  elif message.text == "левая" and state == 3:
        bot.send_message(
            message.from_user.id,
            'Тебе сегодня повезло, однако не думай, что всё так быстро закончится ха-ха-ха',
             reply_markup=ReplyKeyboardMarkup().add("ты это о чём?..." )
        )
        state = 4
  elif message.text == "правая" and state == 3:
        bot.send_message(
            message.from_user.id,
            'Не угадал...) ха-ха-ха, прощай, дружок, наша встреча была прекрасной, но недолгой)))',
        )
  elif message.text == "ты это о чём?..." and state == 4:
        bot.send_message(
            message.from_user.id,
            'Не угадал...) ха-ха-ха, прощай, дружок, наша встреча была прекрасной, но недолгой)))',
        )
    else:
        bot.send_message(
            message.from_user.id,
            'ты мне не нравишься...уходи'
        )



bot.infinity_polling()

