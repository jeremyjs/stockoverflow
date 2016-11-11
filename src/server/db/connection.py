import pymongo

client = pymongo.MongoClient('mongodb://root:rootpass@ds033103.mongolab.com:33103')
db = client['stock-overflow']

truefx_client = pymongo.MongoClient('mongodb://localhost')
truefx = truefx_client['truefx']['ticks']

