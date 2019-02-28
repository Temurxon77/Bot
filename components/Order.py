from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
import telebot

def Ordering():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Buyurma berish',callback_data=f"order"))
    return markup