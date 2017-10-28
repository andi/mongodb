
import pymongo

from pymongo import MongoClient


# connect to database
connection = MongoClient('db', 27017)

db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print item['name']
