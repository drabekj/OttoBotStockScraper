from provider.QuandlClient import QuandlClient
from storage.RDSClient import RDSClient

print("Test")
stockClient = QuandlClient.instance()
df = stockClient.get_test_batch()
print(df)

print("------")
for index, row in df.iterrows():
    print(row.id, row.employee)

# dbClient = RDSClient.instance()
# dbClient.save_batch(data="pandas data")
