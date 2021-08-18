# П.12 из задания "Все классы спрятать в файле"
import requests
import json
from tokens import ACCESS_KEY
from config import keys


class ConvertonExpection(Exception):
    pass


class СurrencyConvertor:
    # Функция конвертации валют
    @staticmethod
    def convetation(quote: str, base: str, amount: str):
        # - имя валюты, цену на которую надо узнать, — base;
        # - имя валюты, цену в  которой надо узнать, — quote;
        # - количество переводимой валюты — amount.
        # values = message.text.split(' ')
        # # Проверка введённых параметров
        # if len(values) != 3:
        #     raise ConvertonExpection('параметров не три')
        #
        # # quote, base, amount  = message.text.split(' ')
        # quote, base, amount = values
        # Проверка одинаковости валют
        if quote == base:
            raise ConvertonExpection('Валюты одинаковые')
        if not amount.isdigit():
            raise ConvertonExpection(f'Не удалось обработать количество {amount} ')
        # Проверка корректности введённых валют
        # #    try:
        #     if quote in keys.keys() and base in keys.keys():
        #         raise ConvertonExpection('Такой валюты нет')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertonExpection(f'Валюты {quote} в списке доступных нет ')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertonExpection(f'Валюты {base} в списке доступных нет ')
        # try:
        #     amount_ticket = float(amount)
        #     # print(amount_ticket)
        # except KeyError:
        #     raise ConvertonExpection(f'Не удалось обработать количество {amount} ')
        # print(keys.get(quote),keys.get(base),amount)
        resault = convertaton_base(quote_ticker, base_ticker, float(amount))
        #    resault = convertaton_base('USD','RUB',100)
        #     print(resault)
        return resault


# Функция конвертации валют от базовой евро
def convertaton_base(quote, base, amount):
    #    try:
    r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={ACCESS_KEY}')
    # #r = requests.get(getval)
    # print(r.status_code)  # узнаем статус полученного ответа
    # print(r.content)

    # Полный список
    texts_all = json.loads(r.content)
    # Список стоимости валют относительно евро, т.к. это бесплатная версия
    texts = texts_all.get('rates')
    # print(type(texts))
    # print(texts)
    #
    # print(texts.get('EUR'))
    # print(texts.get('USD'))
    # print(texts.get('RUB'))
    # print(texts.get(quote))
    # print(texts.get(base))
    # print(amount)
    cost = (texts.get(base) / texts.get(quote)) * amount
    return cost

# convertaton_base('RUB','USD',1)

# print(convertaton_base('USD','RUB',100))
