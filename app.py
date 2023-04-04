from flask import Flask, render_template
from forms import TickerForm
from tickers import ticker_list, add_holding, portfolio_dict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker_form = TickerForm()
    if ticker_form.validate_on_submit():
        ticker = ticker_form.ticker.data
        quantity = ticker_form.quantity.data
        add_holding(ticker, quantity)
        ticker_form.ticker.data = ''
        ticker_form.quantity.data = ''
        
    return render_template('index.html', ticker_form=ticker_form, ticker_list=ticker_list, portfolio_dict=portfolio_dict)

if __name__ == "__main__":
    app.run(debug=True)

