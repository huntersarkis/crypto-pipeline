import requests

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,solana,ripple",
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

response = requests.get(url, params=params)
data = response.json()

for coin, values in data.items():
    print(f"{coin.upper()}: ${values['usd']:,} | 24hr change: {values['usd_24h_change']:.2f}%")