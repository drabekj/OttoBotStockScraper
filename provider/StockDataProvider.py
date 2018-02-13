from abc import ABC, abstractmethod


class StockDataProvider(ABC):
    _instance = None

    @staticmethod
    def instance():
        """ Static access method. """
        if StockDataProvider._instance is None:
            raise Exception("This class is a singleton and hasn't been instantiated yet!")
        return StockDataProvider._instance

    # API interface
    @abstractmethod
    def get_quote(self, ticker, days=7):
        pass

    @abstractmethod
    def get_batch(self, ticker_list):
        pass
