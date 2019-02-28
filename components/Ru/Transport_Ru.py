import telebot
from telebot.types import InlineKeyboardButton,ReplyKeyboardMarkup
from telebot import types


def Transport_Ru():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('Транспорт'))
    markup.row(InlineKeyboardButton('Перевозчик'),InlineKeyboardButton('Эвакуатор'))
    markup.row(InlineKeyboardButton('Грузовики'),InlineKeyboardButton('Тяжелая техника'))
    markup.row(InlineKeyboardButton('Menu'),InlineKeyboardButton('Orqaga'))
    return markup