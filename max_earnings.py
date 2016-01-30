from sortedcontainers import SortedDict
from buy_sell_hold import BUY, SELL, HOLD

# prices: { 'date': price }
# signal_crosses: { 'date': <BUY,SELL,HOLD>}
def max_earnings(prices, signal_crosses, budget=1):
    prices = SortedDict(prices)
    cash_on_hand = budget
    shares = 0
    for date, price in prices.iteritems():
        signal = signal_crosses[date]
        if(signal == SELL):
            shares += cash_on_hand / price
            cash_on_hand = 0
        elif(signal == BUY):
            cash_on_hand += shares * price
            shares = 0
    final_value = max(cash_on_hand, shares * prices.values()[-1])
    earnings = final_value - budget
    return earnings
