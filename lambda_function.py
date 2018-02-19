from provider.QuandlClient import QuandlClient
from storage.RDSClient import RDSClient


def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """
    print("Test")
    stock_client = QuandlClient.instance()
    df = stock_client.get_test_batch()
    print(df)

    storage_client = RDSClient.instance()
    storage_client.save_batch(df)
