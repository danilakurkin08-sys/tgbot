#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from config import API_TOKEN
from telebot.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           Message)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)


button1 = telebot.types.KeyboardButton(text="Кнопка 1")
button2 = telebot.types.KeyboardButton(text="Кнопка 2")
keyboard.add(button1)
keyboard.add(button2)
keyboard.add('1', '2')
# keyboard.row('5', '6', '7')

bot = telebot.TeleBot(API_TOKEN)
print(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    bot.reply_to(message, f'Привет!, {message.from_user.first_name}')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    bot.send_message(
        message.chat.id,
        'hello_message',
        reply_markup=keyboard,
        parse_mode='HTML'
    )


bot.infinity_polling()

