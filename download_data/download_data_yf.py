import pandas as pd
import yfinance as yf

def last_week_month(stock_list,interval, start,end):

    ohlc_data_weekly = []
    for i in stock_list:
        stocks_weekly = yf.download(i, start=start, end=end,
                                      interval=interval, rounding=True)
        stocks_weekly["Symbol"] = i
        ohlc_data_weekly.append(stocks_weekly)

    ohlc_data = update_data(ohlc_data_weekly)
    return ohlc_data


def last_day(stock_list):
    ohlc_data_daily = []
    for i in stock_list:
        stocks_daily = yf.download(i, period="1d", interval="1d", rounding=True)
        stocks_daily["Symbol"] = i
        ohlc_data_daily.append(stocks_daily)

    ohlc_data = update_data(ohlc_data_daily)
    return ohlc_data


def update_data(ohlc_data):
    ohlc_data = pd.concat(ohlc_data)
    ohlc_data = ohlc_data.reset_index()
    ohlc_data = ohlc_data[ohlc_data.isna().any(axis=1) == False]
    ohlc_data.sort_values(by='Symbol', inplace=True)

    return ohlc_data
