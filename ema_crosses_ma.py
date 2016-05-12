from exponential_moving_average import ewmas
from moving_average import moving_averages
from signal_crosses import signal_crosses
from sys import argv
from math import floor

DEFAULT_EMA_PERIOD = 5
DEFAULT_MA_PERIOD = 5

def ema_ma_signal_crosses(prices, ema_period=DEFAULT_EMA_PERIOD, ma_period=False):
    ma_period = ma_period or ema_period
    num_prices = len(prices)
    ma_period = min(ma_period, num_prices)
    if ema_period == DEFAULT_EMA_PERIOD:
        ema_period = min(ema_period, num_prices, int(round(.46*ma_period)))
    ma  = ewmas(prices, ma_period)
    ema = ewmas(prices, ema_period)

    # lists must be the same length
    ema = ema[len(ema)-len(ma):len(ema)]

    return signal_crosses(ema, ma)

def test():
    message = "long_short_signal_crosses"
    cp = [22.27,22.19,22.08,22.17,22.18,22.13,22.23,22.43,22.24,22.29,22.15,22.39,22.18,22.13,22.19,22.08,22.17,22.23,22.43]
    res = ema_ma_signal_crosses(cp, ema_period=5, ma_period=5)
    expected = {'up_crosses': [5, 11], 'down_crosses': [4, 6]}

    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)

    print message

def curr_signal(prices):
    message = "curr_signal"
    currprices = list[-5:]
    sma = (sum(currprices)/5)
    ema = ewmas(prices, 5)
    swap = false 
    i=1
    trend_val = ema-sma
    while(!swap || i < len(prices)-5)
        currprices = prices[-5-i:-i]
        sma = (sum(currprices)/5)
        ema = ewmas(prices, 5)

        if (trend_val < ema-sma)
            swap = true
            return -1
        if (trend_val > ema-sma)
            swap = true
            return 1
        i+=1
        count+=1
        


    return('up_crosses', 'down_crosses')

if(len(argv) > 1 and argv[1] == "test"):
    test()
