from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot


def Settings_Uz():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton("UZ"),InlineKeyboardButton("RU"))
    markup.row(InlineKeyboardButton("Xizmatimizni Baholash"),InlineKeyboardButton("ismni ozgartirish"),InlineKeyboardButton("qaytarish"))
    markup.row(InlineKeyboardButton('Menu'),InlineKeyboardButton('Orqaga'))
    return markup
