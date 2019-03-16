import socketserver
from pymongo import MongoClient

from pyPage.Server import Server

from routes import htmlRoutes, errorRoutes



database = MongoClient('localhost', 27017)['books']

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



def main():
    address = '127.0.0.1'
    port = 8080
    handlerFactory = Server.factory(htmlRoutes, errorRoutes)

    # testing

    with socketserver.TCPServer((address, port), handlerFactory) as httpServer:
        try:
            print(f'HTTP server on ({address}:{port})')
            httpServer.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
