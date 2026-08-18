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

    SPY= SPY.reset_index().pivot(index="Date", columns="Tickers", values="Close")
    IYW= IYW.reset_index().pivot(index="Date", columns="Tickers", values="Close")
    VT = VT.reset_index().pivot(index="Date", columns="Tickers", values="Close")
    DBA= DBA.reset_index().pivot(index="Date", columns="Tickers", values="Close")
    TLT= TLT.reset_index().pivot(index="Date", columns="Tickers", values="Close")
    PDBC= PDBC.reset_index().pivot(index="Date", columns="Tickers", values="Close")
    IAU= IAU.reset_index().pivot(index="Date", columns="Tickers", values="Close")
    

if __name__ == "__main__":
    main()