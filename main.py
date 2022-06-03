from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
import os

app = Flask(__name__)
app.secret_key = 'secret'

apiKey = os.getenv('APIKEY')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            amount = request.form['amount']
            amount = float(amount)
            print(amount)
            from_c = request.form['from_c']
            print(from_c)
            to_c = request.form['to_c']
            print(to_c)
            url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(from_c, to_c, apiKey)
            response = requests.get(url=url).json()
            rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
            rate = float(rate)
            print(rate)
            result = rate * amount
            print(result)
            return render_template('home.html', result=round(result, 2), amount=amount,from_c_code=from_c, from_c_name=from_c,to_c_code=to_c, to_c_name=to_c)
        except Exception as e:
            return '<h1>Bad Request : {}</h1>'.format(e)
  
    else:
        return render_template('home.html')
  
  
if __name__ == "__main__":
    app.run(debug=True)

