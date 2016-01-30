from numpy import sign
from sys import argv
from sortedcontainers import SortedDict

# TODO: proper enum
BUY  =  1
SELL = -1
HOLD =  0

# TODO: rename signal_crosses
def signalCrosses(short_moving_averages, long_moving_averages):
    short_moving_averages = SortedDict(short_moving_averages)
    long_moving_averages = SortedDict(long_moving_averages)

    short_len = len(short_moving_averages.values())
    long_len  = len(long_moving_averages.values())

    if(short_len != long_len):
        print "[Error] signalCrosses: inputs must be same size"
        return {}

    signal_crosses = {}
    last_diff_dir = 0
    for date, short_average in short_moving_averages.iteritems():
        long_average = long_moving_averages[date]
        diff = short_average - long_average

        if(last_diff_dir == 0):
            signal_crosses[date] = HOLD
            if(diff != 0):
                last_diff_dir = sign(diff)
            continue

        if(sign(diff) != last_diff_dir):
            signal_crosses[date] = BUY if last_diff_dir < 0 else SELL
            last_diff_dir = -last_diff_dir
        else:
            signal_crosses[date] = HOLD

    return SortedDict(signal_crosses)

def test():
    message = "signalCrosses"

    s = {'1': 8, '2': 10, '3': 12, '4': 14, '5': 13, '6': 10, '7': 7}
    l = {'1': 9, '2': 10, '3': 11, '4': 13, '5': 12, '6': 11, '7': 8}

    res = signalCrosses(s, l)
    expected = {'1': HOLD, '2': BUY, '3': HOLD, '4': HOLD, '5': HOLD, '6': SELL, '7': HOLD}

    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)

    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
