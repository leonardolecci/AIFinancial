from flask import Flask, render_template
from forms import TickerForm, PortfolioForm
from tickers import ticker_list, add_holding, portfolio_dict
from portfolioOptimizer import calculate_monthly_returns


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
    stock_returns, portfolio_returns, cleaned_weights, sharpe_ratio = calculate_monthly_returns(ticker_list, portfolio_dict)
    portfolio_form = PortfolioForm()
    if portfolio_form.validate_on_submit():
        return render_template('portfolio.html', portfolio_dict=portfolio_dict, ticker_list=ticker_list, stock_returns=stock_returns, portfolio_returns=portfolio_returns, cleaned_weights=cleaned_weights, sharpe_ratio=sharpe_ratio)
    return render_template('index.html', portfolio_form=portfolio_form)

if __name__ == "__main__":
    app.run(debug=True)

