from moving_average import movingAverage
from signal_crosses import signalCrosses

def macd(closing_prices, short_period=12, long_period=26):
    short_ma = movingAverage(closing_prices, short_period)
    long_ma  = movingAverage(closing_prices, long_period)

    return signalCrosses(short_ma, long_ma)
