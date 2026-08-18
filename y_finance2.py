from y_finance import get_stock
import datetime 
from datetime import date, datetime, timezone

def main():

    start = datetime(2023, 1, 1)
    end   = datetime.today()

    # data = get_stock("SPY", start, end)
    # data = data.pivot(index="Date", columns="Ticker", values="Close")
    # print(data.head())

    SPY = get_stock("SPY", start, end)
    IYW= get_stock("IYW", start, end)
    VT = get_stock("VT", start, end)
    DBA = get_stock("DBA", start, end)
    TLT = get_stock("TLT", start, end)
    PDBC = get_stock("PDBC", start, end)
    IAU = get_stock("IAU", start, end)


if __name__ == "__main__":
    main()