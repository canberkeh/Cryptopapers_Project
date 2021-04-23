import requests

url = "https://coingecko.p.rapidapi.com/simple/price"

querystring = {"ids":"btc","vs_currencies":"usd"}

headers = {
    'x-rapidapi-key': "8200c4be52msh500d32be82b9abcp16c7b0jsn847107d6e2f7",
    'x-rapidapi-host': "coingecko.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)