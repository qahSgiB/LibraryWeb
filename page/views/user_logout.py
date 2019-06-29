from pyPage.settings.view import getDefaultSettings

from a.sessionManager import logout



settings = getDefaultSettings()
settings['isRedirect'] = True



def view(getData, postData, cookies, sessionCookie):
    logout(sessionCookie.value)

    return '/', []