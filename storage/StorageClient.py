from abc import ABC, abstractmethod


class StorageClient(ABC):
    _instance = None

    @staticmethod
    def instance():
        """ Static access method. """
        if StorageClient._instance is None:
            raise Exception("This class is a singleton and hasn't been instantiated yet!")
        return StorageClient._instance

    @abstractmethod
    def save_batch(self, data):
        """
        :param data: formated as 2d array=[[info1], [info2], ...] where infoN=[ticker, date, open, high, low, close, volume, ex-dividend, split_ratio, adj_open]
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        e.g.: ['AAPL', '2018-02-16', 172.36, 174.82, 171.77, 172.43, 39638793.0, 0.0, 1.0, 172.36, 174.82, 171.77, 172.43, 39638793.0], ['AAT', '2018-02-16', 32.12, 32.73, 32.12, 32.53, 474175.0, 0.0, 1.0, 32.12, 32.73, 32.12, 32.53, 474175.0]
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        pass
    #
    # @abstractmethod
    # def update(self):
    #     pass
