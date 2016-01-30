from long_short_signal_crosses import long_short_signal_crosses

def simulate(data):
    print data
    res = long_short_signal_crosses(data)
    print res
    return res
