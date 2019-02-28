from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot

def Rate_Ru():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton('1'),InlineKeyboardButton('2'),InlineKeyboardButton('3'),InlineKeyboardButton('4'),InlineKeyboardButton('5'))
    markup.row(InlineKeyboardButton('Меню'),InlineKeyboardButton('Назад'))
    return markup
