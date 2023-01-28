import requests
import json
from config import avaliable_currencies

class ConvertionException(Exception):
    pass

class APIException():
    @staticmethod
    def get_price(currency1: str, currency2: str, amount: str):
    
        if currency1 == currency2:
            raise ConvertionException(f"Невозможно перевести одинаковые валюты {currency1}")

        try:
            currency1_ticker = avaliable_currencies[currency1]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {currency1}")

        try:
            currency2_ticker = avaliable_currencies[currency2]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать ваоюту {currency2}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обрботать количество {amount}")

        request = requests.get(f'https://api.exchangerate.host/convert?from={currency2_ticker}&to={currency1_ticker}')
        exchange_value = json.loads(request.content)["result"]
        return exchange_value