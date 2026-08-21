import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime



def get_stock(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, auto_adjust=False) #auto_adjust to not adjust the closing and have column for the adjust
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_value_levels(0)
    data = data.loc[:, ~data.columns.duplicated()]
    data = data.reset_index()   #to reset index from dates to numbers
    data["Tickers"] = ticker  #for new column called Tickers
    return data

def main():
    start = datetime.datetime(2018, 1,1)
    end = datetime.datetime.today()
    tickers = ["SPY", "VT", "IYW", "TLT", "DBA", "PDBC", "IAU"]

    data = {}

    for i in tickers:
        data[i] = 





if __name__ == "__main__":
    main()
    