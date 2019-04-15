from a.mongo import booksCollection



def findBooks(searchBook):
    def isResult(book, searchBook):
        return True
        # return searchBook == book['title']

    books = booksCollection.find({})
    booksFound = []

    for book in books:
        if isResult(book, searchBook):
            booksFound.append(book)

    return booksFound