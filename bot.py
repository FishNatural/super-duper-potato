import telebot

bot = telebot.TeleBot('987690305:AAHO9BRC7Rv1WdDHn9i65uoF506CykYPNYI')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока', 'я тебя люблю')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, человек')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMkX0ubylz9Sh-TmWWfkB9NOWgkh1cAAgQGAALQhvsKHll6Xzz0_nsbBA')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, человек')



bot.polling()