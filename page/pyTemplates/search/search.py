from pyPage.Template import PyTemplate, HtmlTemplate



def render(resultBookContexts):
    resultBookTemplate = PyTemplate.load('search/searchResult.py')
    resultBooksHtml = resultBookTemplate.formatMultiple(resultBookContexts['results'])

    context = {
        'results': resultBooksHtml,
        'title': resultBookContexts['title'],
    }

    template = HtmlTemplate.load('search/search.html')
    html = template.format(context)

    return html
