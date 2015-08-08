from moving_average import movingAverage
from sys import argv

# either period or multiplier should be named e.g. ema([1,2,3], period=2)
def exponentialMovingAverage(closing_prices, period=None, multiplier=None):
    if(multiplier == None):  multiplier = 2 / (period + 1)
    elif(period == None): period = (2 / multiplier) - 1
    else: print "must provide period or multiplier, but not both"; return;
    ema = []
    ema[0] = movingAverage(closing_prices, period)[0]
    for i in xrange(1, len(closing_prices)):
        close = closing_prices[i]
        prev_ema = ema[i-1]
        ema[i] = (close - prev_ema) * multiplier + prev_ema
    return ema

def ema(closing_prices, period=None, multiplier=None):
    return exponentialMovingAverage(closing_prices, period, multiplier)

def test():
    cp = [22.27,22.19,22.08,22.17,22.18,22.13,22.23,22.43,22.24,22.29,22.15,22.39]
    expected = [22.22, 22.21, 22.24]
    res = exponentialMovingAverage(cp, period=10)
    if(res == expected):
        print "Test Pass"
    else:
        print "Fail: expected", res, "to equal", expected


if(len(argv) > 1 and argv[1] == "test"):
    test()
