from y_finance import get_stock
import datetime 
import pandas as pd
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

    SPY= SPY.reset_index().pivot(index="Date", columns="Ticker", values="Close")
    IYW= IYW.reset_index().pivot(index="Date", columns="Ticker", values="Close")            #not DRY
    VT = VT.reset_index().pivot(index="Date", columns="Ticker", values="Close")
    DBA= DBA.reset_index().pivot(index="Date", columns="Ticker", values="Close")
    TLT= TLT.reset_index().pivot(index="Date", columns="Ticker", values="Close")
    PDBC= PDBC.reset_index().pivot(index="Date", columns="Ticker", values="Close")
    IAU= IAU.reset_index().pivot(index="Date", columns="Ticker", values="Close")
    
    stock = pd.concat([SPY, IYW, VT, DBA, TLT, PDBC, IAU], #pandas  function to join different datas
                      axis=1,  # axis =1 stacks columns horizontally axis =0 satck rows on tops
                      join = "outer") #takes even empty ones and fill missing with NaN
    
    print(stock.head())
if __name__ == "__main__":
    main()