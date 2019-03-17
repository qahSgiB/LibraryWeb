from pymongo import MongoClient



def findBooks(searchBook):
    def isResult(book, searchBook):
        return True
        # return searchBook == book['title']

    books = database['books'].find({})
    booksFound = []

    for book in books:
        if isResult(book, searchBook):
            booksFound.append(book)

    return booksFound



database = MongoClient('localhost', 27017)['books']