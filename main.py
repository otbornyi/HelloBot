import telebot

bot = telebot.TeleBot('7463175667:AAGrh1Qy_VmeGc-xCcgIFSx4_HaoxubJf0o') # токен берем у BotFather


@bot.message_handler(commands = ['start'])
def start(message): # Метод который отвечает на определенное сообщение пользователя
    bot.send_message(message.chat.id, "<b>Привет пользователь!</b>", parse_mode='html') # Что оправляем(в какой чат отсылаем, само сообщение, режим в котором отправляем текст)



bot.polling(none_stop=True)
