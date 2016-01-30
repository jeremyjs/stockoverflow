from flask import Flask
from flask import render_template
from flask import request
from config import keys
import Quandl
import json

from simulate import simulate
from get_prices import get_prices

app = Flask(__name__.split('.')[0])
@app.route('/')
def root():
    return render_template('landing.html')

@app.route('/simulate/<symbol>')
def run_simulation(symbol):
    query_params = request.args
    trim_start = query_params.get('start_date') or '2015-11-01'
    trim_end = query_params.get('end_date') or '2015-12-31'
    prices = get_prices([symbol], trim_start=trim_start, trim_end=trim_end)
    prices = prices[symbol]
    signal_crosses, earnings = simulate(prices)
    dailies = prices
    for timestamp in dailies.keys():
        dailies[timestamp] = { 'price': prices[timestamp], 'signal': signal_crosses[timestamp] }
    signal_crosses = [ [k, v] for k, v in signal_crosses.iteritems()]
    prices = { s: [ [k, v] for k, v in prices[s].iteritems()] for s in prices.keys() }
    return json.dumps({'earnings': earnings, 'dailies': dailies, 'prices': prices, 'signal_crosses': signal_crosses})

@app.route('/<symbol>')
def hello(symbol):
    query_params = request.args
    print (query_params)
    trim_start = query_params.get('start_date') or '2015-12-01'
    trim_end = query_params.get('end_date') or '2015-12-31'
    print (trim_end, trim_start)
    datasets = Quandl.search(symbol, authtoken=keys['quandl'], verbose = False)
    code = datasets[0][u'code']
    data = Quandl.get(code, authtoken=keys['quandl'], collapse='daily', trim_start=trim_start, trim_end=trim_end)
    return data.to_html()

if __name__ == '__main__':
    app.run(debug=True)
