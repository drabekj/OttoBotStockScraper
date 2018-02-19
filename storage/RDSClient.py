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

    def save_batch(self, df):
        connection = self._connect()
        try:
            with connection.cursor() as cursor:
                # Create a new record
                for index, row in df.iterrows():
                    sql = "INSERT INTO `Employee` (`EmpID`, `Name`) VALUES (%s, %s)"
                    cursor.execute(sql, (row.id, row.employee))

            connection.commit()
        finally:
            connection.close()

    def _create_table(self):
        connection = self._connect()

        try:
            with connection.cursor() as cursor:
                # create table
                sql = "CREATE TABLE IF NOT EXISTS Employee ( EmpID  INT NOT NULL, Name VARCHAR(255) NOT NULL, PRIMARY KEY (EmpID))"
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

