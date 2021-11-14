"""
Read daily, weekly and monthly data
Find difference Day close and R@, S2 levels(Daily, Weekly & Monthly)
Filtered only data, weekly or monthly difference in (-5,5) and Close Price > 100
Filtered only data, daily  difference in (-3,3) and Close Price > 100
Export to excel

"""


from datetime import date
import pandas as pd


data_month = pd.read_excel("./processed_data/nifty200_next_m_2111_pivots.xlsx")
data_week = pd.read_excel("./processed_data/nifty200_next_w_1115_pivots.xlsx")
data_day = pd.read_excel("./processed_data/nifty200_next_d_{}{}_pivots.xlsx".format(date.today().month, (date.today().day + 1)))

data_month.rename(columns={'R2': 'R2_M', 'S2': 'S2_M'}, inplace=True)
data_week.rename(columns={'R2': 'R2_W', 'S2': 'S2_W'}, inplace=True)

data = pd.concat([data_day[['Symbol','Close','S2', 'R2']],
                  data_week[['S2_W', 'R2_W']],
                  data_month[['S2_M', 'R2_M']]],
                 axis = 1)

data['Close_S2'] = data['Close'] - data['S2']
data['Close_R2'] = data['Close'] - data['R2']

data['Close_S2_W'] = data['Close'] - data['S2_W']
data['Close_R2_W'] = data['Close'] - data['R2_W']

data['Close_S2_M'] = data['Close'] - data['S2_M']
data['Close_R2_M'] = data['Close'] - data['R2_M']


# data.query(" (-5 < Close_S2 < 5) or (-5 < Close_R2 < 5)
#            " or (-5 < Close_S2_W < 5) or (-5 < Close_R2_W < 5)
#            " or  (-5 < Close_S2_M < 5) or (-5 < Close_R2_M < 5) ", inplace=True)

data_R2S2W = data.query(" (-5 < Close_S2_W < 5) or (-5 < Close_R2_W < 5) or (-5 < Close_S2_M < 5) or (-5 < Close_R2_M < 5) ")
data_R2S2W.query("( Close > 100 )", inplace=True)


data_R2S2W.to_excel("./processed_data/nifty200_next_d_R2S2W.xlsx", index=False)

data_R2S2D = data.query(" (-3 < Close_S2_W < 3) or (-3 < Close_R2< 3) ")
data_R2S2D.query("( Close > 100 )", inplace=True)


data_R2S2D.to_excel("./processed_data/nifty200_next_d_R2S2D.xlsx", index=False)