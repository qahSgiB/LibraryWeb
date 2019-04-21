from pyPage.Template import HtmlTemplate, PyTemplate
from pyPage.Cookie import Cookie
from pyPage.settings.view import getDefaultSettings

from a.sessionManager import checkSessionDecorator
from a.sessionCollection import getSessionUser



settings = getDefaultSettings()


def view(getData, postData, cookies, sessionCookie):
    # user = getSessionUser(sessionCookie.value)

    context = {
        'response': HtmlTemplate.load('main.html').format({}),
        'sessionCookie': sessionCookie,
    }

    return PyTemplate.load('accountBase.py').format(context), []