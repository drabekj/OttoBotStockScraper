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
    def save_batch(self, df):
        """
        :param df: Dataframe formated as:
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                ticker  timestamp   open    high        low     close   volume      ex-dividend  split_ratio    adj_open    adj_high    adj_low adj_close   adj_volume
        None
        0       TSLA    2018-02-06  325.21  336.2200    323.50  333.63  4937928.0   0.0          1.0            325.21      336.2200    323.50  333.63      4937928.0
        1       TSLA    2018-02-07  338.99  346.0000    335.66  345.00  5846823.0   0.0          1.0            338.99      346.0000    335.66  345.00      5846823.0
        2       AMZN    2018-02-06  1444.31 1444.31     1443.60 1443.36 9996464.0   0.0          1.0            343.31      348.6200    314.60  315.36      9996464.0
        3       AMZN    2018-02-07  1448.93 1444.31     1444.76 1444.11 12795099.0  0.0          1.0            319.93      320.9845    294.76  310.11      12795099.0
        4       BOX     2018-02-07  22.13   22.0800     22.25   22.73   6166161.0   0.0          1.0            316.13      318.0800    306.25  315.73      6166161.0
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        pass
    #
    # @abstractmethod
    # def update(self):
    #     pass
