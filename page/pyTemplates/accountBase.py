from pyPage.Template import HtmlTemplate

from a.sessionCollection import getSessionUser



def render(baseContext):
    context = {}

    sessionCookie = baseContext['sessionCookie']
    user = getSessionUser(sessionCookie.value)

    if user == None:
        context['account'] = HtmlTemplate.load('accountBase/logedout.html').format({})
    else:
        context['account'] = HtmlTemplate.load('accountBase/logedin.html').format({})

    response = baseContext['response']

    return HtmlTemplate(response).format(context)