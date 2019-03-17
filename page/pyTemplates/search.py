from pyPage.Template import HtmlTemplate

import importlib.util



def render(resultBookContexts):
    resultBookTemplate = HtmlTemplate.load('search/searchResult.html')
    resultBooksHtml = resultBookTemplate.formatMultiple(resultBookContexts)

    context = {
        'results': resultBooksHtml
    }

    template = HtmlTemplate.load('search/search.html')
    html = template.format(context)

    return html
