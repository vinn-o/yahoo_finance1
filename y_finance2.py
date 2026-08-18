import y_finance
import datetime 
from datetime import date, datetime, timezone
def main():
    ticker = "VT"
    start = datetime(2023, 1, 1)
    end   = datetime.today()

    data = y_finance.get_stock(ticker, start, end)
    print(data)


if __name__ == "__main__":
    main()