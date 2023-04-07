import yfinance as yf
import pandas as pd
import numpy as np
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import objective_functions

def get_prices(ticker_list, time_interval="1mo", type_price="Adj Close"):
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
    weights = pd.Series(portfolio_dict) / sum(portfolio_dict.values())
    return weights

def calculate_monthly_returns(ticker_list, portfolio_dict):
    # Get adjusted close prices for all tickers
    data = yf.download(ticker_list, period="max", interval="1mo", group_by='ticker')['Adj Close']
    
    # Calculate monthly returns
    monthly_returns = data.resample('M').last().pct_change().dropna()
    
    # Calculate monthly returns for each stock
    stock_returns = monthly_returns.mean()
    
    # Calculate total portfolio monthly returns
    weights = pd.Series(portfolio_dict) / sum(portfolio_dict.values())
    portfolio_returns = (monthly_returns * weights).sum(axis=1)
    
    # Calculate Sharpe ratio
    cov_matrix = CovarianceShrinkage(monthly_returns).ledoit_wolf()
    expected_returns = mean_historical_return(monthly_returns)
    ef = EfficientFrontier(expected_returns, cov_matrix)
    ef.add_objective(objective_functions.L2_reg)
    raw_weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    sharpe_ratio = ef.portfolio_performance()[2]
    
    return stock_returns, portfolio_returns, cleaned_weights, sharpe_ratio