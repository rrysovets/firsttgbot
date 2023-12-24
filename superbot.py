import telebot
from telebot.types import Message
import json

bot = telebot.TeleBot(token='6776346152:AAGKICqmGSVofNCpPqQNn-S_QJcMphouX1E')



@bot.message_handler(commands=['жопа'])
def echo(message:Message):
    bot.send_message(chat_id=message.chat.id,text='ты жопа')

dir()
bot.polling()