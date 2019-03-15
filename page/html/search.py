from pyPage.Template import templatePath

from main import database



def render(getData=None, postData=None):
    html = None
    with open(templatePath('search.html'), 'r') as htmlFile:
        html = htmlFile.read()

    searchBook = getData['search']
    print(searchBook)

    books = database['books'].find({})
    bookFound = None

    for book in books:
        if searchBook == book['title']:
            bookFound = book

        if bookFound != None:
            break

    bookHtml = None
    if bookFound == None:
        bookHtml = '<p>Book not found</p>'
    else:
        title = bookFound['title']
        author = bookFound['author']

        bookHtml = f'{title}_{author}'

    context = {
        'book': bookHtml,
    }

    return html.format(**context)
