from abc import ABC, abstractmethod


class StorageClient(ABC):
    _instance = None

    @staticmethod
    def instance():
        """ Static access method. """
        if StorageClient._instance is None:
            raise Exception("This class is a singleton and hasn't been instantiated yet!")
        return StorageClient._instance

    # @abstractmethod
    # def save_batch(self, data):
    #     pass
    #
    # @abstractmethod
    # def update(self):
    #     pass
