from y_finance import get_stock
import datetime 
import pandas as pd
from datetime import date, datetime, timezone
import matplotlib.pyplot as plt


def main():
    start = datetime(2022, 1,1)
    end = datetime.today()

    tickers = ["SPY", "IYW", "VT", "DBA", "TLT", "PDBC", "IAU"]
    # tickers = "SPY"

    data = {}

    for i in tickers:
        data[i] = get_stock(i, start, end).reset_index().pivot(index="Date", columns="Ticker", values="Close")

    # tt = data
    # print(tt.head())

    stock = pd.concat([data[i] for i in tickers],
                      axis=1,
                      join="outer")
    print(stock.head())


    # PPP = stock["SPY"]
    # ppp["previous"] = ppp["Close"].shift(1)

    change1 = (lambda x, y: ((x-y)/y)*100)(stock["SPY"], stock["SPY"].shift(1))

    # plt.hist(change1, bins=50)
    # plt.hist(change1, bins=50)
    ss = change1.cumsum()
    
    plt.show()


if __name__ == "__main__":
    main()  #push  checker
