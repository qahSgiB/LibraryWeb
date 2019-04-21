from pymongo import MongoClient



databases = MongoClient('localhost', 27017)['books']