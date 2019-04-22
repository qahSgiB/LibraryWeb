from pyPage.Template import HtmlTemplate

from a.sessionCollection import getSessionUser



def render(baseContext):
    context = {}

    sessionCookie = baseContext['sessionCookie']
    user = getSessionUser(sessionCookie.value)

    if user == None:
        context['account'] = HtmlTemplate.load('accountBase/logedout.html').format({})
    else:
        firstName = user['first_name']
        lastName = user['last_name']
        name = f'{firstName} {lastName}'

        accountContex = {
            'name': name,
            'mail': user['mail'],
        }

        context['account'] = HtmlTemplate.load('accountBase/logedin.html').format(accountContex)

    response = baseContext['response']

    return HtmlTemplate(response).format(context)