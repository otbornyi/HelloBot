import telebot
from telebot import types

bot = telebot.TeleBot('7463175667:AAGrh1Qy_VmeGc-xCcgIFSx4_HaoxubJf0o') # токен берем у BotFather


@bot.message_handler(commands = ['start'])
def start(message): # Метод который отвечает на определенное сообщение пользователя
    mess = f'Привет, <b>{message.from_user.first_name}</b>' # Создал переменную которая берет никнейм пользователя и привествует его
    bot.send_message(message.chat.id, mess, parse_mode='html') # Что оправляем(в какой чат отсылаем, само сообщение, режим в котором отправляем текст)


#@bot.message_handler()
def get_user_text(message): # Метод который отвечает на любое сообщение пользователя(не команду)
    if message.text == "hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID = {message.from_user.id}", parse_mode='html') # Сообщает юзеру его айди
    elif message.text == "photo":
        photo = open('bash1.png', 'rb')
        bot.send_photo(message.chat.id, photo) # отправляет юзеру картинку
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')

@bot.message_handler(content_types=['photo']) 
def get_user_photo(message):
    bot.send_message(message.chat.id, "Вау, крутое фото") # Принимает картинку пользователя, и отвечает на него 


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.vk.com"))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)
   



bot.polling(none_stop=True)
