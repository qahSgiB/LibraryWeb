from pyPage.Template import PyTemplate
from pyPage.settings.view import getDefaultSettings



settings = getDefaultSettings()



def view(getData, postData, cookies, sessionCookie):
    context = {
        'errorMessage': None,
    }

    if 'error' in getData:
        context['errorMessage'] = getData['error']
        context['mail'] = getData['mail']

    return PyTemplate.load('user_login.py').format(context), []