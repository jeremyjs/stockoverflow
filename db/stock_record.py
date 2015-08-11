from connection import db
import csv

StockRecords = db['stockRecords']

def createStockRecord(record):
    res = StockRecords.insert_one(record)
    id = res.inserted_id
    return StockRecords.find_one({ '_id': id })

# Supports any NYSE ETFs
# interval: 'daily', hourly', 'five_minute'
def importStockRecords(symbol, interval):
    # TODO: validate symbol and interval
    # TODO: smarter root path
    path = '../text_data_sources/nyse_etfs/' + interval + symbol + '.us.txt'
    with open(path, 'rb') as csv_file:
        record_reader = csv.reader(csv_file, delimiter=',', quotechar='')
        for row in record_reader:
            # TODO: read in records
            # TODO: insert records into db
            pass
