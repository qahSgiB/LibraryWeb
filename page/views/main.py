from pyPage.Template import HtmlTemplate



def view(getData, postData):
    context = {}

    return HtmlTemplate.load('main.html').format(context)