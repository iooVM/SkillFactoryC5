import telebot
from tokens import TOKEN
from config import keys
from extensions import convertaton_base
from extensions import ConvertonExpection
from extensions import СurrencyConvertor

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    #    bot.send_message(message.chat.id, f"Welcome, {message.chat.first_name} {message.chat.last_name}")
    #    bot.reply_to(message,f"Welcome, {message.chat.first_name} {message.chat.last_name}")
    bot.reply_to(message, f'Для конвертации валюты введите через пробел: \n\
<имя валюты> <имя конвертируемой валюты> <количество >\n\
Для вывода доступных валют введите  /values')


# обработчик /values
@bot.message_handler(commands=['values'])
def values(message):
    available_currency = 'Доступные Валюты:'
    for key in keys.keys():
        available_currency = '\n'.join((available_currency, key))
    #        print((key))
    #    print(keys)

    bot.reply_to(message, available_currency)

# # Обрабатывается все текстовые сообщения
# @bot.message_handler(content_types=['text', 'audio'])
# def handle_docs_audio(message):
#     print(message.text)
#     pass

# обработка конвертации
@bot.message_handler(content_types=['text', ])
def convetation(message: telebot.types.Message):
    # - имя валюты, цену на которую надо узнать, — base;
    # - имя валюты, цену в  которой надо узнать, — quote;
    # - количество переводимой валюты — amount.
    try:
        values = message.text.split(' ')
        # Проверка введённых параметров
        if len(values) != 3:
            raise ConvertonExpection('параметров не три')
        quote, base, amount = values
        resault = СurrencyConvertor.convetation(quote, base, amount)
    except ConvertonExpection as e:
        bot.reply_to(message, f' Ошибка: {e}')
    else:
        bot.reply_to(message, f' {resault}')


bot.polling(none_stop=True)
