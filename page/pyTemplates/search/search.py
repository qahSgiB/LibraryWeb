from pyPage.Template import PyTemplate, HtmlTemplate



def render(resultBookContexts):
    resultBookTemplate = PyTemplate.load('search/searchResult.py')
    resultBooksHtml = resultBookTemplate.formatMultiple(resultBookContexts)

    context = {
        'results': resultBooksHtml
    }

    template = HtmlTemplate.load('search/search.html')
    html = template.format(context)

    return html
