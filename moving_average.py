from sys import argv

def movingAverage(closing_prices, period=5):
    seq=closing_prices[0:5]
    avg1=sum(seq)/5
    print avg1
    return [avg1,14,15]

def test():
    L=[11,12,13,14,15,16,17]
    result=[13,14,15]
    assert movingAverage(L) == result
    print "Test Pass"

if(len(argv) > 1 and argv[1] == "test"):
    test()
