from datetime import datetime

ticker_list = []
portfolio_dict = {}
purchase_date_dict = {}
sales_date_dict = {}


def add_holding(ticker, quantity, date_purchased, date_sold):
    ticker_list.append(ticker)
    portfolio_dict[ticker] = int(quantity)
    purchase_date_dict[ticker] = date_purchased.strftime('%Y-%m-%d')
    sales_date_dict[ticker] = date_sold.strftime('%Y-%m-%d')

def calculate_markowitz_portfolio():
    pass


