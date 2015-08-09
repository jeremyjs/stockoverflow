def movingAverage(closing_prices, period=5):
    averages=[]
    num_averages=(len(closing_prices))-period+1
    for i in range(num_averages):
        j=i+period
        seq=closing_prices[i:j]
        avg=sum(seq)/period
        avg=round(avg,2)
        averages.append(avg)
    print averages
    return averages


def test():
    L=[11,12,13,14,15,16,17]
    result=[13,14,15]
    assert movingAverage(L) == result
    print "Test Pass"

test()
