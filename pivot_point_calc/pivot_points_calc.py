

def get_cpr_pivots(data_ohlc):

    ##-------------------CPR------------------------------
    data_ohlc['Pivot'] = (data_ohlc['High'] + data_ohlc['Low'] + data_ohlc['Close'])/3
    data_ohlc['BC'] = (data_ohlc['High'] + data_ohlc['Low'])/2
    data_ohlc['TC'] = (data_ohlc['Pivot'] - data_ohlc['BC']) + data_ohlc['Pivot']
    data_ohlc['Pivot_Range'] = abs(data_ohlc['TC'] - data_ohlc['BC'])

    ##-------------------Standard Pivot Points------------------------------
    data_ohlc['R1'] = (2*data_ohlc['Pivot']) - data_ohlc['Low']
    data_ohlc['S1'] = (2*data_ohlc['Pivot']) - data_ohlc['High']
    data_ohlc['R2'] = (data_ohlc['Pivot']) + (data_ohlc['High'] - data_ohlc['Low'])
    data_ohlc['S2'] = (data_ohlc['Pivot']) - (data_ohlc['High'] - data_ohlc['Low'])
    data_ohlc['R3'] = (data_ohlc['R1']) + (data_ohlc['High'] - data_ohlc['Low'])
    data_ohlc['S3'] = (data_ohlc['S1']) - (data_ohlc['High'] - data_ohlc['Low'])
    data_ohlc['R4'] = (data_ohlc['R3']) + (data_ohlc['R2'] - data_ohlc['R1'])
    data_ohlc['S4'] = (data_ohlc['S3']) - (data_ohlc['S1'] - data_ohlc['S2'])

    return data_ohlc


def get_fibo_pivots(data_ohlc):

    #---------------------- Fibo Pivot Points-----------------------
    data_ohlc['Pivot'] = (data_ohlc['High'] + data_ohlc['Low'] + data_ohlc['Close']) / 3
    data_ohlc['R1_Fibo'] = data_ohlc['Pivot'] + (data_ohlc['Range']*0.382)
    data_ohlc['S1_Fibo'] = data_ohlc['Pivot'] - (data_ohlc['Range']*0.382)
    data_ohlc['R2_Fibo'] = data_ohlc['Pivot'] + (data_ohlc['Range']*0.618)
    data_ohlc['S2_Fibo'] = data_ohlc['Pivot'] - (data_ohlc['Range']*0.618)
    data_ohlc['R3_Fibo'] = data_ohlc['Pivot'] + (data_ohlc['Range']*1.000)
    data_ohlc['S3_Fibo'] = data_ohlc['Pivot'] - (data_ohlc['Range']*1.000)

    return data_ohlc


def get_camarilla_pivot(data_ohlc):

    # -------------------Camarilla pivot points------------------------------
    data_ohlc['L1'] = data_ohlc['Close'] - data_ohlc['Range']*(1.1/12)
    data_ohlc['H1'] = data_ohlc['Close'] + data_ohlc['Range']*(1.1/12)
    data_ohlc['L2'] = data_ohlc['Close'] - data_ohlc['Range']*(1.1/6)
    data_ohlc['H2'] = data_ohlc['Close'] + data_ohlc['Range']*(1.1/6)
    data_ohlc['L3'] = data_ohlc['Close'] - data_ohlc['Range']*(1.1/4)
    data_ohlc['H3'] = data_ohlc['Close'] + data_ohlc['Range']*(1.1/4)
    data_ohlc['L4'] = data_ohlc['Close'] - data_ohlc['Range']*(1.1/2)
    data_ohlc['H4'] = data_ohlc['Close'] + data_ohlc['Range']*(1.1/2)
    data_ohlc['H5'] = (data_ohlc['High']/data_ohlc['Low'])*data_ohlc['Close']
    data_ohlc['L5'] = data_ohlc['Close'] - (data_ohlc['H5'] - data_ohlc['Close'])

    return data_ohlc