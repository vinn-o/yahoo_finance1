from y_finance import get_stock
import datetime 
from datetime import date, datetime, timezone

def main():
    ticker = "VT"
    start = datetime(2023, 1, 1)
    end   = datetime.today()

    data = get_stock(ticker, start, end)
    data = data.pivot(index="Date", columns="Ticker", values="Close")
    print(data.head())


if __name__ == "__main__":
    main()