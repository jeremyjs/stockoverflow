from exponential_moving_average import ewmas
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

def lssc_interval(prices, interval):
    interval_multipliers = {
        'DAYS': 1,
        'HOURS': 24,
        'MINUTES': 24*60,
        'SECONDS': 24*60*60
    }
    if isinstance(interval, str): multiplier = interval_multipliers[interval]
    elif isinstance(interval, (int, float)): multiplier = interval
    new_ema_period = DEFAULT_EMA_PERIOD * multiplier
    new_ma_period = DEFAULT_MA_PERIOD * multiplier
    return long_short_signal_crosses(prices, ema_period=new_ema_period, ma_period=new_ema_period)

def lssc_hourly(prices):
    return lssc_interval(prices, 'HOURS')

def test():
    message = "long_short_signal_crosses"
    cp = [22.27,22.19,22.08,22.17,22.18,22.13,22.23,22.43,22.24,22.29,22.15,22.39,22.18,22.13,22.19,22.08,22.17,22.23,22.43]
    res = long_short_signal_crosses(cp, ema_period=3, ema_period=7)
    expected = {'up_crosses': [5, 11], 'down_crosses': [4, 6]}

    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)

    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
