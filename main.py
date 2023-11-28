import telebot

bot = telebot.TeleBot('6928123731:AAGYItuWjBPy9SKOlWu2B3k1AbC4xDBZmIc')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет. Ты попал в космическую шахту. У меня есть команды /info и /info2 !', parse_mode='Markdown')

@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, 'Немного информации о космосе. Космос - это все пространство за пределами Земли, включая звезды, планеты, галактики и все остальное.', parse_mode='Markdown')


@bot.message_handler(commands=['info2'])
def main(message):
    bot.send_message(message.chat.id, 'Подписывайся, чтобы узнать еще больше!', parse_mode='Markdown')

bot.infinity_polling()