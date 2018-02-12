from provider.QuandlClient import QuandlClient

print("Test")
provider = QuandlClient()
data = provider.get_quote("TSLA")
print(data)
