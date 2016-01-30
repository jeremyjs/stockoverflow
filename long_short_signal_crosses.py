from exponential_moving_average import emas
from signal_crosses import signalCrosses
from sys import argv
from math import floor

DEFAULT_SHORT_PERIOD = 12
DEFAULT_LONG_PERIOD  = 26

def long_short_signal_crosses(prices, short_period=DEFAULT_SHORT_PERIOD, long_period=DEFAULT_LONG_PERIOD):
    num_prices = len(prices)
    long_period = min(long_period, num_prices)
    if short_period == DEFAULT_SHORT_PERIOD:
        short_period = min(short_period, num_prices, int(round(.46*long_period)))
    long_ma  = emas(prices, long_period)
    short_ma = emas(prices, short_period)

    # lists must be the same length
    short_ma = short_ma[len(short_ma)-len(long_ma):len(short_ma)]

    return signalCrosses(short_ma, long_ma)

def lssc_interval(prices, interval):
    interval_multipliers = {
        'DAYS': 1,
        'HOURS': 24,
        'MINUTES': 24*60,
        'SECONDS': 24*60*60
    }
    if isinstance(interval, str): multiplier = interval_multipliers[interval]
    elif isinstance(interval, (int, float)): multiplier = interval
    new_short_period = DEFAULT_SHORT_PERIOD * multiplier
    new_long_period = DEFAULT_LONG_PERIOD * multiplier
    return long_short_signal_crosses(prices, short_period=new_short_period, long_period=new_long_period)

def lssc_hourly(prices):
    return lssc_interval(prices, 'HOURS')

def test():
    message = "long_short_signal_crosses"
    cp = [22.27,22.19,22.08,22.17,22.18,22.13,22.23,22.43,22.24,22.29,22.15,22.39,22.18,22.13,22.19,22.08,22.17,22.23,22.43]
    res = long_short_signal_crosses(cp, short_period=3, long_period=7)
    expected = {'up_crosses': [5, 11], 'down_crosses': [4, 6]}

    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)

    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
