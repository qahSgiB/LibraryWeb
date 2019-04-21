from pyPage.Template import HtmlTemplate

from a.sessionCollection import getSessionUser



def render(context):
    renderNext = context['next']
    contextNext = context['context']
    sessionCookie = context['sessionCookie']

    user = getSessionUser(sessionCookie.value)

    if user == None:
        contextNext['account'] = HtmlTemplate('accountBase/logedout.html').format({})
    else:
        contextNext['account'] = HtmlTemplate('accountBase/logedin.html').format({})

    return renderNext.format(contextNext)