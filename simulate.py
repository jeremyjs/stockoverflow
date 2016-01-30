from long_short_signal_crosses import long_short_signal_crosses
from max_earnings import max_earnings
from max_key import max_key

# prices: { date: price }
def simulate(prices, budget=1):
    signal_crosses = long_short_signal_crosses(prices)
    earnings = max_earnings(prices, signal_crosses, budget)
    return signal_crosses, earnings

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
