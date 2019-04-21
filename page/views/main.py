from pyPage.Template import HtmlTemplate
from pyPage.Cookie import Cookie
from pyPage.settings.view import getDefaultSettings

from a.sessionManager import checkSessionDecorator
from a.sessionCollection import getSessionUser



settings = getDefaultSettings()


def view(getData, postData, cookies, sessionCookie):
    # user = getSessionUser(sessionCookie.value)

    context = {}

    return HtmlTemplate.load('main.html').format(context), []