from flask import Flask
from flask import render_template
from flask import request
from sortedcontainers import SortedDict
import Quandl
import json
import sys

sys.path.append('./src')
from simulate import simulate
from get_prices import get_prices
from config import keys

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
    signal_crosses, simulation, earnings = simulate(prices)
    dailies = prices
    for timestamp in dailies.keys():
        dailies[timestamp] = {
            'price': prices[timestamp],
            'signal': signal_crosses[timestamp],
            'shares': simulation[timestamp]['shares'],
            'cash_on_hand': simulation[timestamp]['cash_on_hand']
        }
    dailies = SortedDict(dailies)
    return json.dumps({'earnings': earnings, 'dailies': dailies})

@app.route('/<symbol>')
def hello(symbol):
    query_params = request.args
    trim_start = query_params.get('start_date') or '2015-12-01'
    trim_end = query_params.get('end_date') or '2015-12-31'
    datasets = Quandl.search(symbol, authtoken=keys['quandl'], verbose = False)
    code = datasets[0][u'code']
    data = Quandl.get(code, authtoken=keys['quandl'], collapse='daily', trim_start=trim_start, trim_end=trim_end)
    return data.to_html()

if __name__ == '__main__':
    app.run(debug=True)
