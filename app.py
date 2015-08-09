from flask import Flask
from flask import render_template
from config import keys
import Quandl

app = Flask(__name__.split('.')[0])
@app.route('/')
def root():
    return render_template('landing.html')

@app.route('/<symbol>')
def hello(symbol):
    datasets = Quandl.search(symbol, authtoken=keys['quandl'], verbose = False)
    code = datasets[0][u'code']
    data = Quandl.get(code, authtoken=keys['quandl'], collapse='daily', trim_start='2015-06-01', trim_end='2015-06-30')
    return data.to_html()

if __name__ == '__main__':
    app.run(debug=True)
