import requests
import sys
from provider.StockDataProvider import StockDataProvider


class QuandlClient(StockDataProvider):
    _API_KEY = '7w6LeRcCC_kYpMy4tMpw'

    @staticmethod
    def instance():
        """ Static access method. """
        if StockDataProvider._instance is None:
            QuandlClient()
        return StockDataProvider._instance

    def __init__(self):
        """ Virtually private constructor. """
        if StockDataProvider._instance is not None:
            raise Exception("This class is a singleton! Use method instance() instead")
        else:
            StockDataProvider._instance = self

    def get_all_tickers_info_for_date(self, date):
        """
        Get ticker information about all tickers in DB for the specific date.

        :param date: date to get information about tickers
        :return: 2d array: [[info1], [info2], ...] where infoN=[ticker, date, open, high, low, close, volume, ex-dividend, split_ratio, adj_open]
        """
        param = {
            'api_key': self._API_KEY,
            'date': date,
        }

        try:
            r = requests.get("https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json", params=param)
            r.raise_for_status()

            data = r.json()
        except requests.exceptions.HTTPError as err:
            print("HTTPError: " + str(err))
            sys.exit(1)
        except requests.exceptions.Timeout as err:
            print("Timeout: " + str(err))
            sys.exit(1)
        except requests.exceptions.TooManyRedirects as err:
            print("TooManyRedirects: " + str(err))
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print("RequestException: " + str(err))
            sys.exit(1)

        return data['datatable']['data']
