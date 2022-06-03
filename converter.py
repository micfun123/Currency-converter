import requests
import os

def converter(currenyf,currencyt,amount):
    apiKey = os.getenv('APIKEY')
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(currenyf,currencyt,apiKey)
    r = requests.get(url)
    data = r.json()
    exchange = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    total = float(amount) * float(exchange)
    total = round(total, 2)
    x = "exchange = "+ exchange
    z = "You wanted {}{}".format(amount,currenyf)
    y ="That is {}{}".format(total,currencyt)
    return(x,z,y)
 

print(converter("USD","GBP",5))

