import telebot #Импорт библиотеки
TOKEN = 'Ваш токен' #ТОКЕН
bot = telebot.TeleBot(TOKEN) #Активация бота
@bot.message_handler(content_types=['text'])
def echo(message):
    print(message)#Вывод сообщения
    if message.text == 'Привет':
        bot.send_message(message.chat.id, f'Привет {message.from_user.username}')
    elif message.text == 'Как дела?':
        bot.send_message(message.chat.id, 'Нормально, а у тебя как?')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Пока( 🌧️🌧️🌧️🌧️')
    else:
        bot.send_message(message.chat.id, message.text)
if __name__ == '__main__':
    bot.infinity_polling()