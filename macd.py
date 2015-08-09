from exponential_moving_average import ema
from signal_crosses import signalCrosses

def macd(closing_prices, short_period=12, long_period=26):
    short_ma = emas(closing_prices, short_period)
    long_ma  = emas(closing_prices, long_period)

    return signalCrosses(short_ma, long_ma)
