from moving_average import movingAverages
from sys import argv

# either period or multiplier should be named e.g. emas([1,2,3], period=2)
def exponentialMovingAverages(closing_prices, period=None, multiplier=None):
    if(multiplier == None):  multiplier = 2.0 / (period + 1)
    elif(period == None): period = (2.0 / multiplier) - 1
    else: print "must provide period or multiplier, but not both"; return;
    emas = []
    regular_mas = movingAverages(closing_prices, period)
    emas.append(regular_mas[0])
    for i in xrange(1, len(regular_mas)):
        close = closing_prices[len(closing_prices)-len(regular_mas)+i]
        prev_ema = emas[i-1]
        next_ema = (close - prev_ema) * multiplier + prev_ema
        next_ema = round(next_ema, 2)
        emas.append(next_ema)
    return emas

def emas(closing_prices, period=None, multiplier=None):
    return exponentialMovingAverages(closing_prices, period, multiplier)

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
