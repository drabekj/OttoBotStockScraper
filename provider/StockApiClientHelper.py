from datetime import date, timedelta, datetime
import time


class StockApiClientHelper:
    @staticmethod
    def valid_response(df):
        # print(df)
        try:
            if isinstance(df.loc['timestamp'], datetime):
                timestamp = df.loc['timestamp'].strftime('%Y-%m-%d')
            else:
                timestamp = df.loc['timestamp']

            price_open = str(df.loc['open'])

            if timestamp != str(date.today()) and timestamp != str(date.today() - timedelta(1)):
                print("Error: Data is not forom today. timestamp=" + timestamp)
                return False
            if StockApiClientHelper.is_number(price_open) is not True or price_open == 0:
                print("Error: Price is not valid. price=" + price_open)
                return False

            return True
        except:
            print(df)
            raise

    @staticmethod
    def is_number(s):
        try:
            i = float(s)
            # check if its NaN
            if i != i:
                return False
            return True
        except ValueError:
            return False

    @staticmethod
    def write_to_csv(execution_time, valid, req_type, file_name="test.csv"):
        with open(file_name, 'a+') as ofile:
            # 'timestamp', 'execution_time', 'valid', 'price', "type"
            timestamp = str(time.time())
            execution_time = str(execution_time)
            valid = str(valid)

            ofile.write(timestamp + "," + execution_time + "," + valid + "," + req_type + "\n")

    @staticmethod
    def print_response(res):
        print('HTTP/1.1 {status_code}\n{headers}\n\n{body}'.format(
            status_code=res.status_code,
            headers='\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
            body=res.text,
        ))
