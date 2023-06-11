import json
from pandas import read_json
from binance import Client

from .config import API_KEY, SECRET_KEY


def binance_api():
    try:
        client = Client(api_key=API_KEY,
                        api_secret=SECRET_KEY)

        data = json.dumps(client.get_symbol_ticker())
        df = read_json(data)
        df.to_csv('./flaskr/db/symbol_ticker.csv', encoding='utf-8', index=False)

        client.close_connection()
    except Exception as e:
        print(e)
