from sys import argv

def moving_averages(prices, period=5):
    len_prices = len(prices)
    if(len_prices < period):
        print "moving_averages: `period` must be less than number of `prices`"
        return []
    averages=[]
    num_averages = len_prices - period + 1
    for i in range(num_averages):
        j=i+period
        seq=prices[i:j]
        avg=sum(seq)/period
        avg=round(avg,2)
        averages.append(avg)
    # print averages
    return averages


def test():
    message = "moving_averages"
    L=[11,12,13,14,15,16,17]
    expected = [13,14,15]
    res = moving_averages(L)
    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)
    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
