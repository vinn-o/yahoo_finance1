import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def get_stock(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, auto_adjust=False)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_value_levels(0)
        
    