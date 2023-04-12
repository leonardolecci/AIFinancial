from flask import Flask, render_template
from forms import TickerForm, PortfolioForm
from tickers import ticker_list, add_holding, portfolio_dict
from portfolioOptimizer import get_prices, get_weights, get_returns, get_average_total_returns, get_average_monthly_returns


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker_form = TickerForm()
    portfolio_form = PortfolioForm() 
    if ticker_form.validate_on_submit():
        ticker = ticker_form.ticker.data
        quantity = ticker_form.quantity.data
        add_holding(ticker, quantity)
        ticker_form.ticker.data = ''
        ticker_form.quantity.data = ''
        
    return render_template('index.html', ticker_form=ticker_form, ticker_list=ticker_list, portfolio_dict=portfolio_dict, portfolio_form=portfolio_form)


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    data = get_prices(ticker_list)
    weights = get_weights(portfolio_dict)
    monthly_returns = get_returns(data, weights)
    avg_returns = get_average_total_returns(data, ticker_list)

    portfolio_form = PortfolioForm()
    if portfolio_form.validate_on_submit():
        return render_template('portfolio.html', portfolio_dict=portfolio_dict, ticker_list=ticker_list, data = data, weights = weights,  monthly_returns=monthly_returns, avg_returns = avg_returns, portfolio_form=portfolio_form)
    return render_template('index.html', portfolio_form=portfolio_form)

if __name__ == "__main__":
    app.run(debug=True)

