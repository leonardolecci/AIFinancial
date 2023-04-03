from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    tickers = request.form['tickers']
    amounts = request.form['amounts']
    # Call the Yahoo finance API to get descriptions of the user's holdings
    # and return the results to the user
    api_url = f"https://finance.yahoo.com/quote/{tickers}/analysis?p={tickers}"
    response = requests.get(api_url)
    response_json = response.json()
    results = []
    for ticker, amount in zip(tickers.split(','), amounts.split(',')):
        description = response_json['description']
        results.append(f"{ticker}: {description}")
    return jsonify(results=results)

if __name__ == '__main__':
    app.run(debug=True)
