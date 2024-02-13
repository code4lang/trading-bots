import requests
url = "https://api.bitpanda.com/v1/ticker"
response = requests.get(url)
data = response.json()

btc_price = data['BTC']

print(btc_price)
