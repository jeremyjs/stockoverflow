import pymongo

client = pymongo.MongoClient('mongodb://root:rootpass@ds151707.mlab.com:51707/stockoverflow')
db = client['stockoverflow']

truefx_client = pymongo.MongoClient('mongodb://localhost')
truefx = truefx_client['truefx']['ticks']
