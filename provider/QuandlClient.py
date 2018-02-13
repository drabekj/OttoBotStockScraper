import datetime
import quandl
import time
import pandas as pd
from provider.StockApiClientHelper import StockApiClientHelper
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
        quandl.ApiConfig.api_key = self._API_KEY

        if StockDataProvider._instance is not None:
            raise Exception("This class is a singleton! Use method instance() instead")
        else:
            StockDataProvider._instance = self

    def get_quote(self, ticker, days=7):
        """
        Return historical data (from current date - :param days till now) of given stock (:param ticker).
        :param ticker: requested stock ticker symbol
        :param days: number of days into the past to get data
                    eg. days=7 returns stock info from today till today-7 days
        :return: df (ticker, timestamp, open, high, low, close, volume)
        """
        data = self.__get_time_series_daily(ticker, days=days)
        return data

    def get_multiple_sequence(self, ticker_list):
        print("Get multiple daily prices of quotes: " + str(ticker_list))

        start_time = time.time()
        data = pd.DataFrame()
        for quote in ticker_list:
            data = data.append(self.__get_time_series_daily(quote), ignore_index=True)
        end_time = time.time()
        execution_time = end_time - start_time

        # print(data)
        # print("Execution time: " + str(execution_time) + " seconds")
        valid = False
        for index, row in data.iterrows():
            valid = StockApiClientHelper.valid_response(data.iloc[index])
            if valid is False:
                break

        StockApiClientHelper.write_to_csv(execution_time, valid, "M", file_name="output/output_m.csv")
        return data

    def get_batch(self, ticker_list):
        print("Get batch of quotes: " + str(ticker_list))
        start_time = time.time()
        data = self.__get_batch_data(ticker_list)
        end_time = time.time()
        execution_time = end_time - start_time

        # print("Execution time: " + str(execution_time) + " seconds")
        valid = False
        for index, row in data.iterrows():
            valid = StockApiClientHelper.valid_response(row)
            if valid is False:
                break

        StockApiClientHelper.write_to_csv(execution_time, valid, "B", file_name="output/output_b.csv")
        return data

    # noinspection PyMethodMayBeStatic
    def __get_time_series_daily(self, ticker, days=7):
        """
        Get stock data for the last :param days
        :param ticker:
        :param days: no. of days how much historical data will be returned
        :return:
        """
        start_date = datetime.date.today() - datetime.timedelta(days)
        data = quandl.get_table('WIKI/PRICES', ticker=ticker, date={'gte': start_date})

        data.rename(columns={'date': 'timestamp'}, inplace=True)
        # last_entry = data.iloc[-1]

        return data

    # noinspection PyMethodMayBeStatic
    def __get_batch_data(self, ticker_list):
        start_date = datetime.date.today() - datetime.timedelta(7)
        data = quandl.get_table('WIKI/PRICES', ticker=ticker_list, date={'gte': start_date})

        data.rename(columns={'date': 'timestamp'}, inplace=True)

        # get only the most recent entries for each ticker
        last_timestamp = data.iloc[-1]['timestamp']
        data = data.loc[data['timestamp'] == last_timestamp]

        return data
