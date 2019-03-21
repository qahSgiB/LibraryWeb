from pyPage.Template import HtmlTemplate



def render(resultBookContext):
    availableText = None
    available = resultBookContext['available']

    if available > 0:
        availableText = f'{available} pieces available'
    elif resultBookContext['available'] == 0:
        availableText = 'Item is currently not avialable'

    context = {
        'title': resultBookContext['title'],
        'author': resultBookContext['author'],
        'availableText': availableText,
    }

    resultBookTemplate = HtmlTemplate.load('search/searchResult.html')

    return resultBookTemplate.format(context)

