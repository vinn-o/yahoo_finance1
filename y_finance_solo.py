import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import datetime



def get_stock(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, auto_adjust=False) #auto_adjust to not adjust the closing and have column for the adjust
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    data = data.loc[:, ~data.columns.duplicated()]
    data = data.reset_index()   #to reset index from dates to numbers
    data["Tickers"] = ticker  #for new column called Tickers
    return data

def concata(tickers, start, end):
    tickers = tickers
    data = {}
    for i in tickers:
        data[i] = get_stock(i, start, end).pivot(index="Date", columns="Tickers", values="Close")  # one loop for DRY,
    
            # tickers are added to each i in get_stock and placed in the library
    s = pd.concat([data[i] for i in tickers],
                       axis=1,
                       join="outer")
    return s

def main():
    start = datetime(2018, 1,1)
    end = datetime.today()
    tickers = ["SPY", "VT", "IYW", "TLT", "DBA", "PDBC", "IAU"] #all the tickers

    s = concata(tickers, start, end)
    print(s.head())




if __name__ == "__main__":
    main()
    