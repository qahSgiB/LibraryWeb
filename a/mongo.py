from pymongo import MongoClient



databases = MongoClient('localhost', 27017)['books']

booksCollection = databases['books']
usersCollection = databases['users']