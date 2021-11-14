"""
Load Config.json file to load stocks
Download data from  Yfinance- Current day, week and month
Add next day/week/month Pivot levels to data-frame
Export data to excel sheet
"""


from datetime import date
import pandas as pd
import json
from download_data.download_data_yf import *
from pivot_point_calc.pivot_points_calc import *



# Reading Config.json file
with open('./config.json', 'r') as f:
    config = json.load(f)

nifty_50_list = config['nifty50_list']
nifty_200_list = config['nifty200_list']

# Daily Data
data_ohlc_daily = last_day(nifty_200_list)
data_ohlc_daily_pivot = get_cpr_pivots(data_ohlc=data_ohlc_daily)
data_ohlc_daily_pivot.to_excel("./processed_data/nifty200_next_d_{}{}_pivots.xlsx".format(date.today().month, (date.today().day + 1)), index=False)
print("Exported Daily data")

## Monthly Data(Run last day of month)
# data_ohlc_monthly = last_week_month(nifty_200_list,interval="1mo",start="2021-10-01", end="2021-10-31")
# data_ohlc_monthly_pivot = get_cpr_pivots(data_ohlc=data_ohlc_monthly)
# data_ohlc_monthly_pivot.to_excel("./processed_data/nifty200_next_m_2111_pivots.xlsx", index=False)
print("Exported Monthly data")

## Weekly Data (run last day of week- Friday)
# data_ohlc_weekly = last_week_month(nifty_200_list, interval="1wk", start="2021-11-08", end="2021-11-12")
# data_ohlc_weekly_pivot = get_cpr_pivots(data_ohlc=data_ohlc_weekly)
# data_ohlc_weekly_pivot.to_excel("./processed_data/nifty200_next_w_1115_pivots.xlsx", index=False)
print("Exported Weekly data")
