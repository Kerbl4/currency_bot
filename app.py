import telebot

TOKEN = "5894990770:AAGdFWVhzRBRZSxc8j05g3JHSghvGf1C9ds"

bot = telebot.TeleBot(TOKEN)

avaliable_currencies = {
    'Доллар': "USD",
    'Евро': "EUR",
    'Рубль': "RUB"
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')
    text = "Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')
    text = "Доступные валюты:"
    for key in avaliable_currencies.keys():
        text = "\n".join((text, key))
        print(text)
    bot.reply_to(message, text)

bot.polling()