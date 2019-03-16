from pyPage.Template import Template

from main import findBooks



def render(getData=None, postData=None):
    searchBook = getData['search']
    resultBooks = findBooks(searchBook)

    resultBookContexts = []
    for resultBook in resultBooks:
        resultBookContexts.append({
            'title': resultBook['title'],
            'author': resultBook['author'],
            'available': resultBook['available'],
        })

    resultBookTemplate = Template.load('search/searchResult.html')
    resultBooksHtml = resultBookTemplate.formatMultiple(resultBookContexts)

    context = {
        'results': resultBooksHtml,
    }

    template = Template.load('search/search.html')

    return template.format(context)
