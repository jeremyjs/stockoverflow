# prices: { 'date': price }
# signal_crosses: { 'date': <BUY,SELL,HOLD>}
def max_earnings(prices, signal_crosses, budget=1):
    earnings = budget
    shares = 0
    for date, price in prices:
        signal = signal_crosses[date]
        if(signal == BUY):
            shares = earnings / price
            earnings = 0
        elif(signal == SELL):
            earnings = shares * price
            shares
    return earnings
