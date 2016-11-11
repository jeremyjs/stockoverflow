import sys
import quandl
import json

sys.path.append('../../')
from config import keys as auth_keys

argv = sys.argv

def get_code(symbol):
    datasets = Quandl.search(symbol, authtoken=auth_keys['quandl'], verbose = False)
    code = datasets[0][u'code']
    return code

def get_prices(symbols, trim_start='2015-12-01', trim_end='2015-12-31'):
    prices = {}
    for symbol in symbols:
        code = get_code(symbol)
        input_data = Quandl.get(code, authtoken=auth_keys['quandl'], collapse='daily', trim_start=trim_start, trim_end=trim_end)
        input_data = input_data.to_json()
        input_data = json.loads(input_data)
        close_prices = input_data['Close'] if 'Close' in input_data else input_data['CLOSE']
        prices[symbol] = close_prices
    return prices

def test():
    message = "get_prices"

    symbols = ['AAPL', 'TSLA']

    # TODO: mock/stub Quandl api calls
    res = get_prices(symbols, trim_start='2015-12-01', trim_end='2015-12-02')
    expected = {'AAPL':[117.339996, 116.279999], 'TSLA':[237.190002, 231.990005]}

    if(res == expected):
        message = "[....] " + message
    else:
        message = "[FAIL] " + message + ": Expected " + str(res) + " to equal " + str(expected)

    print message

if(len(argv) > 1 and argv[1] == "test"):
    test()
