import telebot
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton
from telebot import types 


def Language():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('RU',callback_data=f"ru"),InlineKeyboardButton('UZ'))
    return markup