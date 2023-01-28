import telebot
from config import avaliable_currencies, TOKEN
from extensions import ConvertionException, APIException

bot = telebot.TeleBot(TOKEN)

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

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
                raise ConvertionException("Кол-во вводимых параметров не равно трём!")

        base, quote, amount = values
        exchange_value = APIException.get_price(base, quote, amount)
    except ConvertionException as exeption:
        bot.reply_to(message, f"Ошибка пользователя.\n{exeption}")
    except Exception as exeption:
        bot.reply_to(message, f"Не удалось обработать команду\n{exeption}")
    else:
        output_text = f"Цена {amount} {base} в {quote} = {exchange_value}"
        bot.send_message(message.chat.id, output_text)

bot.polling()