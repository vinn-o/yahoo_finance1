import pandas as pd
import yfinance as yf
import numpy as np
import datetime
from datetime import time, datetime, timezone

def get_stock(ticker, start, end):
    data = yf.download(ticker, start=start,end=end, auto_adjust=False)
    if isinstance(data.columns, pd.MultiIndex): #checks if object data.columns is of type pd.MultiIndex
        data.columns = data.columns.get_level_values(0)
    data = data.loc[:, ~data.columns.duplicated()] #uses ~ (bitwise NOT operator) that flips duplicates from false to true
    data = data.reset_index()
    data["Ticker"] = ticker #creates a new column named ticker
    return data




    
def main():
    start = datetime(2026, 1, 1)
    end = datetime.today()
    ticker = "IYW" # IYW track U.S technology company market capitalization index
    d = get_stock(ticker, start, end)
    # print(d.head())
    d = d.pivot(index="Date", columns="Ticker", values="Close") #pivot changes the outlook of final data
    print(d.head())

    


if __name__ == "__main__":
    main()