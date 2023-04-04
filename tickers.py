ticker_list = []
portfolio_dict = {}


def add_holding(ticker, quantity):
    ticker_list.append(ticker)
    portfolio_dict[ticker] = quantity