# Start importing
import telebot
from telebot import types 
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,KeyboardButton

def Main_Uz():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.add(types.KeyboardButton('SOS',request_location=True),types.InlineKeyboardButton('Qo\'ng\'iroq'))
    markup.add(types.InlineKeyboardButton('Operator'))
    markup.add(types.InlineKeyboardButton('Xizmatlar',callback_data="services"))
    markup.add(types.InlineKeyboardButton('Ma\'lumotlar',callback_data="info"),types.InlineKeyboardButton('sozlamalar'))
    return markup
