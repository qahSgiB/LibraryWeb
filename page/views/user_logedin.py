from pyPage.settings.view import getDefaultSettings

from a.usersCollection import tryLogin
from a.sessionManager import login



settings = getDefaultSettings()
settings['isRedirect'] = True



def view(getData, postData, cookies, sessionCookie):
    mail = postData['mail']
    password = postData['password']

    loginSuccesful, details = tryLogin(mail, password)

    if loginSuccesful:
        userId = details['user']['id']

        login(sessionCookie.value, userId)

        return '/', []
    else:
        errorMessage = details['errorMessage']
        
        return f'/user/login?error={errorMessage}&mail={mail}', []