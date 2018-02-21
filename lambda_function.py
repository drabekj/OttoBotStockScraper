from provider.QuandlClient import QuandlClient
from storage.RDSClient import RDSClient
from datetime import datetime, timedelta


def handler(event, context):
    # get data from API
    yesterday_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    data = QuandlClient.instance().get_all_tickers_info_for_date(yesterday_date)

    # save stock data to DB
    db_client = RDSClient.instance()
    db_client.save_batch(data)
    print("Data for " + yesterday_date + " added to table")

    return "Scraping successful"
