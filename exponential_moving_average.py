from moving_average import moving_averages
from sys import argv
import pandas

def default_period_multiplier(period=None, multiplier=None):
    if(period == None): period = (2.0 / multiplier) - 1
    elif(multiplier == None):  multiplier = 2.0 / (period + 1)
    else: print "must provide period or multiplier, but not both"; return;
    return (period, multiplier)

# emas: Exponential Moving Averages
# either period or multiplier should be provided e.g. emas([1,2,3], period=2)
def emas(prices, period=None, multiplier=None):
    period, multiplier = default_period_multiplier(period, multiplier)
    emas = []
    regular_mas = moving_averages(prices, period)
    emas.append(regular_mas[0])
    for i in xrange(1, len(regular_mas)):
        close = prices[len(prices)-len(regular_mas)+i]
        prev_ema = emas[i-1]
        next_ema = (close - prev_ema) * multiplier + prev_ema
        next_ema = round(next_ema, 2)
        emas.append(next_ema)
    return emas

# ewmas: Exponential Weighted Moving Averages
# either period or multiplier should be provided e.g. emas([1,2,3], period=2)
def ewmas(prices, period=None, multiplier=None):
    period, multiplier = default_period_multiplier(period, multiplier)
    price_series = pandas.Series(data=prices)
    ewmas = pandas.ewma(price_series, span=period)
    return ewmas

def test():
    message = "exponentialMovingAverages"
    cp = [22.27,22.19,22.08,22.17,22.18,22.13,22.23,22.43,22.24,22.29,22.15,22.39]
    expected = [22.22, 22.21, 22.24]
    res = exponentialMovingAverages(cp, period=10)
    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)
    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
