from exponential_moving_average import emas
from signal_crosses import signalCrosses
from sys import argv

def macd(closing_prices, short_period=12, long_period=26):
    short_ma = emas(closing_prices, short_period)
    long_ma  = emas(closing_prices, long_period)

    return signalCrosses(short_ma, long_ma)

def test():
    message = "macd"
    cp = [22.27,22.19,22.08,22.17,22.18,22.13,22.23,22.43,22.24,22.29,22.15,22.39]
    res = macd(cp)
    print(res)
    return
    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)
    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
