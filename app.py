from flask import Flask
from flask import render_template
from flask import request
from config import keys
import Quandl

app = Flask(__name__.split('.')[0])
@app.route('/')
def root():
    return render_template('landing.html')

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
