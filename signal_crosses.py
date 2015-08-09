from numpy import sign
from sys import argv

def signalCrosses(short_moving_averages, long_moving_averages):
    short_len = len(short_moving_averages)
    long_len  = len(long_moving_averages)
    if(short_len != long_len):
        print "[Error] signalCrosses: input lists must be same length"
        return []
    ma_len = short_len
    up_crosses = []
    down_crosses = []
    last_diff_dir = 0
    start = 0
    for i in xrange(0, ma_len-1):
        diff = short_moving_averages[i] - long_moving_averages[i]
        if(diff != 0):
            start = i
            last_diff_dir = sign(diff)
            break
    for i in xrange(start, ma_len-1):
        new_diff = short_moving_averages[i] - long_moving_averages[i]
        if(sign(new_diff) != last_diff_dir):
            if(last_diff_dir < 0):
                up_crosses.append(i)
            else:
                down_crosses.append(i)
            last_diff_dir = -last_diff_dir
    return { "up_crosses": up_crosses, "down_crosses": down_crosses }

def test():
    message = "signalCrosses"
    s = [8, 10, 12, 14, 13, 10, 7]
    l = [9, 10, 11, 13, 12, 11, 8]
    res = signalCrosses(s, l)
    expected = {'up_crosses': [1], 'down_crosses': [5]}
    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)
    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
