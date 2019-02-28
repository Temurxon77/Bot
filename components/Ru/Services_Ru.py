# import dependencies

import telebot 
from telebot import types
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton

def Services_Ru():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('Сантехник'),InlineKeyboardButton('Электрик'))
    markup.row(InlineKeyboardButton('Транспорт'),InlineKeyboardButton('Программист'))
    markup.row(InlineKeyboardButton('Переводчик'),InlineKeyboardButton('Сварщик'))
    markup.row(InlineKeyboardButton('Меню'),InlineKeyboardButton('Назад'))
    return markup