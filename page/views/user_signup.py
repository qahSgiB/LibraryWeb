from pyPage.Template import HtmlTemplate
from pyPage.settings.view import getDefaultSettings



settings = getDefaultSettings()



def view(getData, postData, cookies, sessionCookie):
    context = {}

    return HtmlTemplate.load('user_signup.html').format(context), []