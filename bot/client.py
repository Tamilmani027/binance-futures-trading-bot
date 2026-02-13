from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
import logging

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logging.info("Binance Futures Testnet client initialized.")

    def place_order(self, **params):
        try:
            logging.info(f"Sending order request: {params}")
            response = self.client.futures_create_order(**params)
            logging.info(f"Order response: {response}")
            return response
        except (BinanceAPIException, BinanceOrderException) as e:
            logging.error(f"Binance error: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            raise
