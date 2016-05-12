from long_short_signal_crosses import long_short_signal_crosses
from max_key import max_key
from sortedcontainers import SortedDict
from buy_sell_hold import BUY, SELL, HOLD

# prices: { 'date': price }
# signal_crosses: { 'date': <BUY,SELL,HOLD>}
def simulation(prices, signal_crosses, budget):
    simulation = {}
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
        simulation[date] = { 'shares': shares, 'cash_on_hand': cash_on_hand }
    final_value = max(cash_on_hand, shares * prices.values()[-1])
    earnings = final_value - budget
    return simulation, earnings


# prices: { date: price }
def simulate(prices, budget=1):
    signal_crosses = long_short_signal_crosses(prices)
    sim, earnings = simulation(prices, signal_crosses, budget)

    return signal_crosses, sim, earnings

# prices: { 'SYMB': { date: price } }
def simulated_earnings(prices, budget=1):
    earnings = {}
    for symbol, prices in prices.iteritems():
        earnings[symbol] = simulate(prices, budget)
    return earnings

# prices: { 'SYMB': { date: price } }
def winner(prices, budget=1):
    earnings = simulated_earnings(prices, budget)
    winner = max_key(earnings)
    return winner
