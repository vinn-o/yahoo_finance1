from y_finance import get_stock
import datetime 
import pandas as pd
from datetime import date, datetime, timezone


def main():
    start = datetime(2025, 1, 1)
    end = datetime.today()

    tickers = ["SPY", "IYW", "VT", "DBA", "TLT", "PDBC", "IAU"]  #all tickers in one list for DRY
    data = {}

    for i in tickers:
        data[i] = get_stock(i, start, end)

    for i in tickers:
        data[i] = data[i].reset_index().pivot(index="Date", columns="Ticker", values="Close")

    df = pd.concat([data[i] for i in tickers],
                   axis =1,
                   join ="outer")
    print(df.head())





if __name__ == "__main__":
    main()