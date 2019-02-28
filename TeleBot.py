# update = Updater(API_TOKEN)
# dispatcher = update.dispatcher

# # Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

# def start(bot,update):
#     bot.send_message(chat_id=update.message.chat_id,text="Start!")
#     Main_Menu_UZ(bot,update)

# def Main_Menu_UZ(bot,update):
#     #isSelected = False
#     buttons = [
#         [KeyboardButton("Location",request_location=True),
#         KeyboardButton("Channel",request_location=False),
#         KeyboardButton("Dispatcher",request_location=False)],
#         [KeyboardButton("Xizmatlar",request_location=False)],
#         [KeyboardButton("Ma\'lumotlar",request_location=False),
#         KeyboardButton("Sozlamalar",request_location=False)]
#     ]
#     reply_markup = ReplyKeyboardMarkup(buttons)
#     bot.send_message(chat_id=update.effective_message.chat_id,text="Main Menu:",reply_markup=reply_markup)
#     #print(update.message.KeyboardButton.value=="Xizmatlar")
#     print(update.effective_message.text)
#     if ():
#         Services_Uz(bot,update)

# def Services_Uz(bot,update):
#     button_service = [
#         [KeyboardButton("Santexnik",request_location=True),
#         KeyboardButton("Elektrik",request_location=False)],
#         [KeyboardButton("Transport",request_location=False),
#         KeyboardButton("Programmist",request_location=False)],
#         [KeyboardButton("Tarjimon",request_location=False),
#         KeyboardButton("Payvandlovchi",request_location=False)]
#     ]
#     reply_markup = ReplyKeyboardMarkup(button_service)
#     bot.send_message(chat_id=update.message.chat_id,text="Xizmat turlari:",reply_markup=reply_markup)

# services_uz_handler = CommandHandler("serviceUz",Services_Uz)
# dispatcher.add_handler(services_uz_handler)

# main_menu_uz = CommandHandler("menuUz",Main_Menu_UZ)
# dispatcher.add_handler(main_menu_uz)

# start_handler = CommandHandler("start",start)
# dispatcher.add_handler(start_handler)


# update.start_polling()
# update.idle()

# import telebot
# from telebot import types


# bot = telebot.TeleBot(API_TOKEN)

# #User Data
# user_dict = {}

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.age = None
#         self.gender = None


# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     msg = bot.reply_to(message, """\What's your name?""")
#     bot.register_next_step_handler(msg, process_name_step)


# def process_name_step(message):
#     try:
#         chat_id = message.chat.id
#         name = message.text
#         user = User(name)
#         user_dict[chat_id] = user
#         msg = bot.reply_to(message, 'How old are you?')
#         bot.register_next_step_handler(msg, process_age_step)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')


# def process_age_step(message):
#     try:
#         chat_id = message.chat.id
#         age = message.text
#         if not age.isdigit():
#             msg = bot.reply_to(message, 'Age should be a number. How old are you?')
#             bot.register_next_step_handler(msg, process_age_step)
#             return
#         user = user_dict[chat_id]
#         user.age = age
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
#         markup.add('Male', 'Female')
#         msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
#         bot.register_next_step_handler(msg, process_sex_step)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')


# def process_sex_step(message):
#     try:
#         chat_id = message.chat.id
#         gender = message.text
#         user = user_dict[chat_id]
#         if (gender == u'Male') or (gender == u'Female'):
#             user.gender = gender
#         else:
#             raise Exception()
#         bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.gender)
#         Insert_Data(user)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')
# def Insert_Data(user):
#     try:
#         conn = mysql.connector.connect(user='root',password='',host='127.0.0.1',database=user_data)
#         cursor = conn.cursor()
#         insert_query = """INSERT INTO 'users' ('Name',) """
#         result = cursor.execute()

# # Enable saving next step handlers to file "./.handlers-saves/step.save".
# # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# # saving will hapen after delay 2 seconds.
# bot.enable_save_next_step_handlers(delay=2)

# # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# # WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

# bot.polling()

# This example show how to use inline keyboards and process button presses
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup,InlineKeyboardButton,KeyboardButton,InlineKeyboardMarkup

# Buttons and Keyboards (UZ)
from components.Uz.Main_frame_Uz import Main_Uz
from components.Uz.Services_Uz import Services_Uz
from components.Uz.Info_Uz import Rate_Uz
from components.Uz.settings_Uz import Settings_Uz
from components.Uz.Transport_Uz import Transport_Uz


# Button and Keyboards (RU)
from components.Ru.Main_frame_Ru import Main_Ru
from components.Ru.Services_Ru import Services_Ru
from components.Ru.Info_Ru import Rate_Ru
from components.Ru.settings_Ru import Settings_Ru
from components.Ru.Transport_Ru import Transport_Ru
from components.Language import Language
from components.Uz.Order_uz import Order_Uz

import mysql.connector
import time
API_TOKEN = '673343206:AAGJ4ryyfzGIlN7Jz-wYmJS-wkTZR4JgZkw'

bot = telebot.TeleBot(API_TOKEN)
 
lang ="uz"
user_dict = {}
isLoggedIn = False




@bot.message_handler()
def Languages(message):
    bot.disable_save_next_step_handlers()
    print(user_dict)
    bot.send_message(message.chat.id,'Tanlang:', reply_markup=Language())
    if message.text == 'UZ':
        lang = "uz"
        bot.register_next_step_handler(message, send_welcome_uz)
    elif message.text == 'RU':
        lang = "ru"
        bot.register_next_step_handler(message,send_welcome_uz)


@bot.message_handler(commands=['help', 'start'])
def send_welcome_uz(message):
    bot.disable_save_next_step_handlers()
    bot.clear_step_handler(message)
    msg = bot.reply_to(message, """Ismingizni kiriting:""")
    bot.register_next_step_handler(msg, process_name_step_uz)


@bot.message_handler(commands=['help', 'start'])
def process_name_step_uz(message):
    bot.disable_save_next_step_handlers()
    try:
        chat_id = message.chat.id
        name = message.text
        user_dict["chat_id"] = message.chat.id
        user_dict["name"] = name
        msg = bot.reply_to(message,'Raqamingizni kiriting')
        bot.register_next_step_handler(msg, process_phone_step_uz) 
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(commands=['help', 'start'])
def process_phone_step_uz(message):
    try:
        chat_id = message.chat.id
        phone = message.text
        if not phone.isdigit():
            msg = bot.reply_to(message, 'phone should be a number...')
            bot.register_next_step_handler(msg, process_phone_step_uz)
            return
        user_dict["phone"] = str(phone)
        bot.send_message(message.chat.id,'Tanlang:', reply_markup=Language())
        bot.send_message(chat_id,'Mal\'umotlarinigiz Saqlanib qoldi || Ваши данные были сохранены')
        bot.register_next_step_handler(message,start_uz)
    except Exception as e:
        bot.reply_to(message, 'oooops')



@bot.message_handler(commands=['start_uz'])
def start_uz(message):
    try:
        bot.disable_save_next_step_handlers()
        bot.register_next_step_handler(message, Main_Page_handler_Uz)
        bot.send_message(message.chat.id, 'Tanlang:', reply_markup=Main_Uz())
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['start_ru'])

def start_ru(message):
    try:
        bot.disable_save_next_step_handlers()
        bot.register_next_step_handler(message, Main_Page_handler_Ru)
        bot.send_message(message.chat.id, 'Выберите:', reply_markup=Main_Ru())
    # bot.disable_save_next_step_handlers()
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['main'])
def Main_Page_handler_Uz(message):
    try:
        bot.disable_save_next_step_handlers()
        chat_id = message.chat.id
        msg = message.text
        if msg == 'Xizmatlar':
            bot.register_next_step_handler(message, Service_Page_handler_Uz)
            bot.send_message(chat_id, "Xizmatlar", reply_markup=Services_Uz())
        elif msg == 'Xizmatni Baholash':
            bot.send_message(chat_id, 'Baho', reply_markup=Rate_Uz())
            #print('main')
        elif msg == 'sozlamalar':
            #print('main')
            bot.register_next_step_handler(message,Settings_handler_Uz)
            bot.send_message(chat_id, 'Sozlamalar', reply_markup=Settings_Uz())
            #print('main')
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(commands=['main'])
def Main_Page_handler_Ru(message):
    try:
        bot.disable_save_next_step_handlers()
        chat_id = message.chat.id
        msg = message.text
        if msg == 'Сервисы':
            bot.register_next_step_handler(message,Service_Page_handler_Ru)
            bot.send_message(chat_id, "Сервисы", reply_markup=Services_Ru())
        elif msg == 'Оценить Сервис':
            bot.send_message(chat_id, 'Оценка', reply_markup=Rate_Ru())
        elif msg == 'Настройки':
            bot.send_message(chat_id, 'Настройки', reply_markup=Settings_Ru())
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['service'])
def Service_Page_handler_Uz(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    msg = message.text
    if msg == 'Orqaga':
        bot.register_next_step_handler(message,Main_Page_handler_Uz)
        bot.send_message(message.chat.id, 'Tanlang:', reply_markup=Main_Uz())
    elif msg == 'Menu':
        bot.register_next_step_handler(message,Main_Page_handler_Uz)
        bot.send_message(message.chat.id, 'Tanlang:', reply_markup=Main_Uz())
    elif msg == 'Elektrik':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering"))
        bot.send_message(chat_id,'Elektrik xizmati',reply_markup=markup)
        bot.send_message(message.chat.id, 'Elektrik',reply_markup=Services_Uz())
        bot.register_next_step_handler(message, Service_Page_handler_Uz)
        #Select_Data_DB(message)
    elif msg == 'Transport': 
        #Inserting_Uz(message)
        
        bot.send_message(chat_id, 'Transport', reply_markup=Transport_Uz())
        bot.register_next_step_handler(message, Transport_Page_handler_Uz)
        print('service')
    elif msg == 'Santexnik':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering"))
        bot.send_message(chat_id,'Santexnik xizmati',reply_markup=markup)
        bot.send_message(message.chat.id, 'Santexnik',reply_markup=Services_Uz())
        bot.register_next_step_handler(message, Service_Page_handler_Uz)
        #Inserting_Uz(message)
    elif msg == 'Programmist':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering"))
        bot.send_message(chat_id,'Programmist xizmati',reply_markup=markup)
        bot.send_message(message.chat.id, 'Programmist',reply_markup=Services_Uz())
        bot.register_next_step_handler(message, Service_Page_handler_Uz)
        #Inserting_Uz(message)
    elif msg == 'Tarjimon':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering"))
        bot.send_message(chat_id,'Tarjimon xizmati',reply_markup=markup)
        bot.send_message(message.chat.id, 'Tarjimon',reply_markup=Services_Uz())
        bot.register_next_step_handler(message, Service_Page_handler_Uz)
        #Inserting_Uz(message)
    elif msg == 'Payvandlovchi':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Buyurtma Berish',callback_data=f"ordering"))
        bot.send_message(chat_id,'Payvandlovchi xizmati',reply_markup=markup)
        bot.send_message(message.chat.id, 'Payvandlovchi',reply_markup=Services_Uz())
        bot.register_next_step_handler(message, Service_Page_handler_Uz)
        #Inserting_Uz(message)


@bot.message_handler(commands=['service'])
def Service_Page_handler_Ru(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    if message.text == 'Назад':
        bot.register_next_step_handler(message,start_ru)
        bot.send_message(chat_id,'Основное Меню', reply_markup=Main_Ru())
    elif message.text == 'Меню':
        bot.register_next_step_handler(message,start_ru)
        bot.send_message(chat_id,'Основное Меню', reply_markup=Main_Ru())
    elif message.text == 'Электрик':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering"))
        bot.send_message(chat_id,'Сервис Электрика',reply_markup=markup)
        #Inserting_Ru(message)
        bot.send_message(chat_id,'Электрик', reply_markup=Services_Ru())
        bot.register_next_step_handler(message, Service_Page_handler_Ru)
        #Select_Data_DB(message)
    elif message.text == 'Транспорт':
        #Inserting_Ru(message)
        bot.send_message(chat_id, 'Транспорт', reply_markup=Transport_Ru())
        bot.register_next_step_handler(message, Transport_Page_handler_Ru)
    elif message.text == 'Сантехник':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering"))
        bot.send_message(chat_id,'Сервис Сантехника',reply_markup=markup)
        #Inserting_Ru(message)
        bot.send_message(chat_id, 'Сантехник', reply_markup=Services_Ru())
        bot.register_next_step_handler(message, Service_Page_handler_Ru)
    elif message.text == 'Программист':
        #Inserting_Ru(message)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering"))
        bot.send_message(chat_id,'Сервис Программиста',reply_markup=markup)
        bot.send_message(chat_id, 'Программист', reply_markup=Services_Ru())
        bot.register_next_step_handler(message, Service_Page_handler_Ru)
    elif message.text == 'Переводчик':
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering"))
        bot.send_message(chat_id,'Сервис Переводчика',reply_markup=markup)
        #Inserting_Ru(message)
        bot.send_message(chat_id, 'Переводчик', reply_markup=Services_Ru())
        bot.register_next_step_handler(message, Service_Page_handler_Ru)
    elif message.text == 'Сварщик':
        #Inserting_Ru(message)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering"))
        bot.send_message(chat_id,'Сервис Сварщика',reply_markup=markup)
        bot.send_message(chat_id, 'Сварщик', reply_markup=Services_Ru())
        bot.register_next_step_handler(message, Service_Page_handler_Ru)


@bot.message_handler(commands=['transport'])
def Transport_Page_handler_Ru(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    if message.text == 'Назад':
        bot.send_message(chat_id, 'Transport', reply_markup=Services_Ru())
        bot.register_next_step_handler(message, Service_Page_handler_Ru)
    elif message.text == 'Меню':
        bot.register_next_step_handler(message, start_ru)
    elif message.text == 'Транспорт':
        bot.send_message(chat_id, 'Транспорт', reply_markup=Transport_Ru())
        bot.register_next_step_handler(message, Transport_Page_handler_Ru)

@bot.message_handler()
def Settings_handler_Uz(message):
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    if message.text == "Xizmatimizni Baholash":
        print('phone number data...')
    elif message.text == "ismni ozgartirish":
        # insert data to SQl database
        print('change name...')
    elif message.text == "Orqaga":
        bot.send_message(chat_id,'Asosiy Menu',reply_markup=Main_Uz())
        bot.register_next_step_handler(message,Main_Page_handler_Uz)
    elif message.text == "Menu":
        bot.send_message(chat_id,'Asosiy Menu',reply_markup=Main_Uz())
        bot.register_next_step_handler(message,Main_Page_handler_Uz)
    elif message.text == "RU":
        bot.register_next_step_handler(message,Main_Page_handler_Ru)
        bot.send_message(chat_id,'Asosiy Menu',reply_markup=Main_Ru())
    elif message.text == "UZ":
        bot.register_next_step_handler(message,Main_Page_handler_Uz)
        bot.send_message(chat_id,'Asosiy Menu',reply_markup=Main_Uz())
    
    
@bot.message_handler(commands=['transport'])
def Transport_Page_handler_Uz(message):
    print('transport')
    bot.disable_save_next_step_handlers()
    chat_id = message.chat.id
    print('transport')
    if message.text == 'Orqaga':
        bot.register_next_step_handler(message,Service_Page_handler_Uz)
        bot.send_message(chat_id,'Xizmatlar', reply_markup=Services_Uz())
    elif message.text == 'Menu':
        bot.send_message(chat_id, 'Menu', reply_markup=Main_Uz())
        bot.register_next_step_handler(message, start_uz)
    elif message.text == 'Yetkazish':
        bot.send_message(chat_id, 'Yetkazish', reply_markup=Transport_Uz())
        bot.register_next_step_handler(message, Transport_Page_handler_Uz)
    elif message.text == 'Evakuator':
        bot.register_next_step_handler(message, Transport_Page_handler_Uz)
        bot.send_message(chat_id, 'Evakuator', reply_markup=Transport_Uz())
    elif message.text == 'Yuk tashuvchi':
        bot.register_next_step_handler(message, Transport_Page_handler_Uz)
        bot.send_message(chat_id, 'Yuk tashuvchi', reply_markup=Transport_Uz())
    elif message.text == 'Og\'ir texnika':
        bot.register_next_step_handler(message, Transport_Page_handler_Uz)
        bot.send_message(chat_id, 'Og\'ir texnika', reply_markup=Transport_Uz())

@bot.message_handler()
def Info_Uz_handler(message):
    if message.text == '1':
        print('1')
    elif message.text == '2':
        print('2')
    elif message.text == '3':
        print('3')
    elif message.text == '4':
        print('4')
    elif message.text == '5':
        print('5')

@bot.callback_query_handler(func=lambda call:True)
def Ordering(call):
    if call.data == "ordering":
        #Insert_Data_DB(call.message)
        #print(call.message)
        bot.answer_callback_query(call.id, "Buyurtmanigiz qabul qilindi...")
        Inserting_Uz(call.message)
    if call.data == "ru":
        bot.send_message(call.message.chat.id,'ru clicked',reply_markup=Services_Uz())

@bot.message_handler(content_type=['text'])
def Insert_Data_DB(message):
    #print('DB')
    bot.disable_save_next_step_handlers()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="ordering"
    )
    chat_id = message.chat.id
    mycursor = mydb.cursor()
    
    name = user_dict["name"]
    phone = user_dict["phone"]
    chat_id = user_dict["chat_id"]
    orders = user_dict['orders']
    sql = """INSERT INTO orders (full_name,order_type,user_name,phone) VALUES (%s,%s,%s,%s) """
    values = (name,orders,chat_id,phone)
    mycursor.execute(sql,values)
    mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)
    bot.register_next_step_handler(message, Service_Page_handler_Uz)


def Inserting_Ru(message):
    if isLoggedIn:
        bot.disable_save_next_step_handlers()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="ordering"
        )
        chat_id = message.chat.id
        mycursor = mydb.cursor()
        sql1 = """SELECT full_name,user_name,phone FROM orders WHERE user_name="""+message.chat.id
        mycursor.execute(sql1)
        myresult = mycursor.fetchone()
        user_dict["name"] = myresult[0]
        user_dict["chat_id"] = myresult[1]
        user_dict["phone"] = myresult[2]
        mydb.commit()
    else:
        chat_id = message.chat.id
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Заказать',callback_data=f"ordering"))
        user_dict["orders"] = message.text
        text = "Name: " + user_dict["name"] + "Chat ID: " + str(user_dict["chat_id"]) + "phone: " + str(user_dict["phone"]) + "Order:"+user_dict["orders"] 
        Insert_Data_DB(message)
        #text = "Name: " + user_dict["name"] + "Chat ID: " + str(user_dict["chat_id"]) + "phone: " + str(user_dict["phone"]) + "Order:"+user_dict["orders"] 
        bot.send_message(47833754,text)
        bot.send_message(chat_id,'Выберите',reply_markup=markup)


def Inserting_Uz(message):
    if isLoggedIn:
        bot.disable_save_next_step_handlers()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="ordering"
        )
        chat_id = message.chat.id
        mycursor = mydb.cursor()
        sql1 = """SELECT full_name,user_name,phone FROM orders WHERE user_name="""+message.chat.id
        mycursor.execute(sql1)
        myresult = mycursor.fetchone()
        user_dict["name"] = myresult[0]
        user_dict["chat_id"] = myresult[1]
        user_dict["phone"] = myresult[2]
        mydb.commit()
    else:
        chat_id = message.chat.id
        user_dict["orders"] = message.text
        text = "Name: " + user_dict["name"] + "Chat ID: " + str(user_dict["chat_id"]) + "phone: " + str(user_dict["phone"]) + "Order:"+user_dict["orders"] 
        Insert_Data_DB(message)
        #text = "Name: " + user_dict["name"] + "Chat ID: " + str(user_dict["chat_id"]) + "phone: " + str(user_dict["phone"]) + "Order:"+user_dict["orders"] 
        #bot.send_message(47833754,text)



bot.polling(none_stop=True)
