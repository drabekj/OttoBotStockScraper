from provider.QuandlClient import QuandlClient

print("Test")
provider = QuandlClient()
data = provider.get_quote("TSLA", 100)
print(data)
