from flask import Flask
from flask import render_template
from flask import request
from config import keys
import Quandl
import json

from simulate import simulate

app = Flask(__name__.split('.')[0])
@app.route('/')
def root():
    return render_template('landing.html')

@app.route('/simulate/<symbol>')
def graph(symbol):
    query_params = request.args
    print (query_params)
    trim_start = query_params.get('start_date') or '2015-12-01'
    trim_end = query_params.get('end_date') or '2015-12-31'
    print (trim_end, trim_start)
    datasets = Quandl.search(symbol, authtoken=keys['quandl'], verbose = False)
    code = datasets[0][u'code']
    input_data = Quandl.get(code, authtoken=keys['quandl'], collapse='daily', trim_start=trim_start, trim_end=trim_end)
    input_data = input_data.to_json()
    input_data = json.loads(input_data)
    close_prices = input_data['Close']
    close_prices = close_prices.values()
    data = simulate(close_prices)
    return json.dumps(data)

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
