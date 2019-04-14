from pyPage.Template import HtmlTemplate



def view(getData, postData, cookies):
    context = {}

    return HtmlTemplate.load('user_signup.html').format(context), []