import requests
import json
from config import avaliable_currencies

class ConvertionException(Exception):
    pass

class APIException():
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
    
        if base == quote:
            raise ConvertionException(f"Невозможно перевести одинаковые валюты {base}")

        try:
            base_ticker = avaliable_currencies[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:
            quote_ticker = avaliable_currencies[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обрботать количество {amount}")

        request = requests.get(f'https://api.exchangerate.host/convert?from={quote_ticker}&to={base_ticker}')
        exchange_value = json.loads(request.content)["result"]
        return exchange_value