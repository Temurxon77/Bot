# import dependencies

import telebot 
from telebot import types
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton

def Services_Uz():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('Santexnik'),InlineKeyboardButton('Elektrik'))
    markup.row(InlineKeyboardButton('Transport'),InlineKeyboardButton('Programmist'))
    markup.row(InlineKeyboardButton('Tarjimon'),InlineKeyboardButton('Payvandlovchi'))
    markup.row(InlineKeyboardButton('Menu'),InlineKeyboardButton('Orqaga'))
    return markup