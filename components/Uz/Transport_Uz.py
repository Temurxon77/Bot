import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types


def Transport_Uz():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('Transport'))
    markup.row(InlineKeyboardButton('Yetkazish'),InlineKeyboardButton('Evakuator'))
    markup.row(InlineKeyboardButton('Yuk tashuvchi'),InlineKeyboardButton('Og\'ir texnika'))
    markup.row(InlineKeyboardButton('Menu'),InlineKeyboardButton('Orqaga'))
    return markup