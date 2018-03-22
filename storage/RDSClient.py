from storage.StorageClient import StorageClient
from storage import rds_config
import logging
import sys
import pymysql


class RDSClient(StorageClient):
    # rds settings
    rds_host = "ottobotdb.clccaawfuuph.eu-central-1.rds.amazonaws.com"
    name = rds_config.db_username
    password = rds_config.db_password
    db_name = rds_config.db_name

    logger = logging.getLogger()

    @staticmethod
    def instance():
        """ Return reference to storage client, if no table exists, create it. """
        if StorageClient._instance is None:
            RDSClient()
        return StorageClient._instance

    def __init__(self):
        """ Virtually private constructor. """
        if StorageClient._instance is not None:
            raise Exception("This class is a singleton! Use method instance() instead")
        else:
            StorageClient._instance = self

        self.logger.setLevel(logging.INFO)
        self._create_table()

    def save_batch(self, data):
        connection = self._connect()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                for stock_entry in data:
                    sql = "INSERT IGNORE INTO `Stock` (`Ticker`, `Date`, `Open`, `High`, `Low`, `Close`, `Volume`, `ExDividend`, `SplitRatio`, `AdjOpen`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (stock_entry[0], stock_entry[1], stock_entry[2], stock_entry[3], stock_entry[4], stock_entry[5], stock_entry[6], stock_entry[7], stock_entry[8], stock_entry[9]))

            connection.commit()
        finally:
            connection.close()

    def _create_table(self):
        connection = self._connect()

        try:
            with connection.cursor() as cursor:
                # create table
                sql = """CREATE TABLE IF NOT EXISTS Stock (
                        Ticker  VARCHAR(5) NOT NULL,
                        Date VARCHAR(10) NOT NULL,
                        Open FLOAT NOT NULL,
                        High FLOAT NOT NULL,
                        Low  FLOAT NOT NULL,
                        Close FLOAT NOT NULL,
                        Volume FLOAT NOT NULL,
                        ExDividend FLOAT NOT NULL,
                        SplitRatio FLOAT NOT NULL,
                        AdjOpen FLOAT NOT NULL,
                        PRIMARY KEY (Ticker, Date)
                    )"""
                cursor.execute(sql)
                self.logger.info("SUCCESS: Table ready")
        finally:
            connection.close()

    def _connect(self):
        try:
            connection = pymysql.connect(self.rds_host, user=self.name, passwd=self.password, db=self.db_name)
        except:
            self.logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
            sys.exit()

        self.logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
        return connection

