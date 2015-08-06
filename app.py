from flask import Flask
from config import keys
import Quandl

app = Flask(__name__)

@app.route("/<symbol>")
def hello(symbol):
  datasets = Quandl.search(symbol, authtoken=keys['quandl'])
  code = datasets[0][u'code']
  data = Quandl.get(code, authtoken=keys['quandl'], collapse='daily')
  print data
  return data.head()

if __name__ == "__main__":
  app.run(debug=True)
