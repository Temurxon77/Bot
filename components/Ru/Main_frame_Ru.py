# Start importing
import telebot
from telebot import types 
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton

def Main_Ru():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.add(types.KeyboardButton('Местонахождение',request_location=True),types.InlineKeyboardButton('Звонок'))
    markup.add(types.InlineKeyboardButton('Оператор'))
    markup.add(types.InlineKeyboardButton('Сервисы',callback_data=f"services"))
    markup.add(types.InlineKeyboardButton('Информация',callback_data="info"),types.InlineKeyboardButton('Настройки'))
    return markup
