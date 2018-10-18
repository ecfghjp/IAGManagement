from pymongo import MongoClient

#initialise mongo client
client = MongoClient('localhost', 27017)
db = client['pymongo_test']

