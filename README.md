# pivot_point_analysis

Purpose: 

Analysis of daily stock price of nifty 50 and nifty 200 stocks based on pivot points.
Select Stocks from NIFY 50, NIFTY 200, which are closer to R2 and S2 levels.

export_to_excel.py: 
- Read config.json file
- Download current day, week and month data from yfinance of nifty 50 and nifty 200 stocks.
- Calculate next day, week and month pivot levels,
- Export data to excel sheet(daily, weekly and monthly) and save all excel sheet in directory- processed_data.

pivot_point_analysis:
- Read the input Excel files(daily, weekly and monthly) processed from above steps.
- Extract Symbol, Close Price(daily), R2 and S2 levels from daily, weekly and monthly sheets.
- Calculate the difference between Close(daily) and R2 Level, Close(daily) and S2 Level.
- Filtered the stocks- Closing price is near to R2 or S2 levels(daily, weekly and monthly)
- Export the filtered data to Excel sheet.
