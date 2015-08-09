from sys import argv

def movingAverages(closing_prices, period=5):
    averages=[]
    num_averages=(len(closing_prices))-period+1
    for i in range(num_averages):
        j=i+period
        seq=closing_prices[i:j]
        avg=sum(seq)/period
        avg=round(avg,2)
        averages.append(avg)
    # print averages
    return averages


def test():
    message = "movingAverages"
    L=[11,12,13,14,15,16,17]
    expected = [13,14,15]
    res = movingAverages(L)
    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)
    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
