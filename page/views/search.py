from pyPage.Template import PyTemplate
from pyPage.settings.view import getDefaultSettings

from a.booksCollection import findBooks



settings = getDefaultSettings()



def view(getData, postData, cookies, sessionCookie):
    searchBook = getData['search']
    resultBooks = findBooks(searchBook)

    resultBookContexts = {
        'title': f'Search | \"{searchBook}\"',
        'results': []
    }

    for resultBook in resultBooks:
        resultBookContexts['results'].append({
            'title': resultBook['title'],
            'author': resultBook['author'],
            'available': resultBook['available'],
        })

    return PyTemplate.load('search/search.py').format(resultBookContexts), []