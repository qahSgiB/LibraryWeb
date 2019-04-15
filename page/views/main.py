from pyPage.Template import HtmlTemplate
from pyPage.Cookie import Cookie
from pyPage.settings.view import getDefaultSettings



settings = getDefaultSettings()



def view(getData, postData, cookies):
    context = {}

    # for cookie in cookies:
    #     print(cookie.name, cookie.value)

    # sendCookies = []

    # for cookie in cookies:
    #     testinCookie = Cookie(cookie.name, cookie.value)
    #     testinCookie.setExpirationTimeY(0)
    #     sendCookies.append(testinCookie)


    return HtmlTemplate.load('main.html').format(context), []