from pyPage.Template import PyTemplate

from a.a import findBooks



def view(getData, postData):
    searchBook = getData['search']
    resultBooks = findBooks(searchBook)

    resultBookContexts = []
    for resultBook in resultBooks:
        resultBookContexts.append({
            'title': resultBook['title'],
            'author': resultBook['author'],
            'available': resultBook['available'],
        })

    return PyTemplate.load('search/search.py').format(resultBookContexts)