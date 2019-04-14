from pyPage.Template import PyTemplate

from a.a import findBooks



def view(getData, postData, cookies):
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