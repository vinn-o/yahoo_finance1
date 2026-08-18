import pandas as pd
import y_finance as yf
import numpy as np
import datetime
from datetime import time, datetime, timezone

def get_stock(ticker, start, end):
    data = yf.download(ticker, start=start,end=end, auto_adjust=False)
def main():
    start = datetime(2026, 1, 1)
    end = datetime.today()
    ticker = "IYW" # IYW track U.S technology company market capitalization index
    d = get_stock(ticker, start, end)

    


if __name__ == "__main__":
    main()