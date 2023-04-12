import yfinance as yf
import pandas as pd
import numpy as np
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import objective_functions


def get_prices(ticker_list, time_interval="1d", type_price="Adj Close"):
    """
    Downloads historical stock prices for a list of tickers from Yahoo Finance
    
    Args:
    ticker_list: list of str representing the stock tickers to download prices for
    time_interval: str representing the interval of historical prices to download (default is "1d" for daily prices)
    type_price: str representing the type of price to download (default is "Adj Close" for adjusted closing price)
    
    Returns:
    A pandas DataFrame containing the historical prices for the given list of tickers and price type
    
    """
    # Get adjusted close prices for all tickers
    data = yf.download(ticker_list, period="240mo", interval=time_interval, group_by='ticker')
    ticker_mod = []
    i = 0
    for item in ticker_list:
        ticker_mod.append((item,type_price))
        i += 1
    data = data[ticker_mod]
    return data

def get_weights(portfolio_dict):
    """
    Calculates the weights for a given portfolio
    
    Args:
    portfolio_dict: dictionary containing the ticker names as keys and their respective weights as values
    
    Returns:
    A pandas Series containing the weights for the given portfolio
    
    """
    weights = pd.Series(portfolio_dict) / sum(portfolio_dict.values())
    return weights

def get_returns(data, weights):
    """
    Calculates the monthly returns and portfolio returns for a given portfolio
    
    Args:
    data: pandas DataFrame containing historical stock prices
    weights: pandas Series containing the weights for the given portfolio
    
    Returns:
    A pandas DataFrame containing the monthly returns and portfolio returns for the given portfolio
    
    """
    monthly_returns = data.resample('D').last().pct_change(25).resample('M').last()
    portfolio_returns = (monthly_returns * weights.values).sum(axis=1)
    monthly_returns['Portfolio Returns'] = portfolio_returns
    return monthly_returns


def get_average_total_returns(data, ticker_list):
    """
    Computes the average total returns for given stock tickers
    
    Args:
    data: pandas DataFrame containing historical stock prices
    ticker_list: list of strings representing the stock tickers for which average total returns are to be calculated
    
    Returns:
    A dictionary with ticker names as keys and average total returns as values for the given stock tickers
    
    """
    avg_total_returns = {}
    for ticker in ticker_list:
        returns = data[ticker].pct_change().dropna()
        start_price = data[ticker].dropna().iloc[0][0]
        end_price = data[ticker].dropna().iloc[-1][0]
        total_returns = (end_price - start_price) / start_price
        num_years = len(returns) / 252 # assuming trading days per year is 252
        avg_annual_total_returns = (1 + total_returns) ** (1 / num_years) - 1
        avg_total_returns[ticker] = avg_annual_total_returns
    return avg_total_returns

def get_average_monthly_returns(data, ticker_list, start_date, end_date):
    """
    Computes the average monthly returns for given stock tickers within a specified period
    
    Args:
    data: pandas DataFrame containing historical stock prices
    ticker_list: list of strings representing the stock tickers for which average monthly returns are to be calculated
    start_date: str representing the start date in the format 'yyyy-mm-dd'
    end_date: str representing the end date in the format 'yyyy-mm-dd'
    
    Returns:
    A dictionary with ticker names as keys and average monthly returns as values for the given stock tickers within the specified period
    
    """
    avg_monthly_returns = {}
    for ticker in ticker_list:
        stock_data = data[ticker].dropna()[start_date:end_date]
        returns = stock_data.pct_change().dropna()
        avg_monthly_returns[ticker] = returns.mean()
    return avg_monthly_returns