from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton
import telebot


def Settings_Ru():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    markup.row(InlineKeyboardButton("UZ"),InlineKeyboardButton("RU"),InlineKeyboardButton("ENG"))
    markup.row(InlineKeyboardButton("Добавить номер"),InlineKeyboardButton("Изменить Имя"),InlineKeyboardButton("Сброс"))
    markup.row(InlineKeyboardButton('Меню'),InlineKeyboardButton('Назад'))
    return markup
