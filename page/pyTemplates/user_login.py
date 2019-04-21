from pyPage.Template import HtmlTemplate



def render(userloginContext):
    errorMessage = userloginContext['errorMessage']

    errorMessageX = ''
    errorMail = ''

    if errorMessage != None:
        mail = userloginContext['mail']

        if errorMessage == 'user_not_found':
            errorMessageX = HtmlTemplate.load('user_login/error_message.html').format({'errorText': 'User not found'})
        elif errorMessage == 'wrong_password':
            errorMail = mail
            errorMessageX = HtmlTemplate.load('user_login/error_message.html').format({'errorText': f'Wrong password'})
        else:
            errorMessageX = 'Unknown error'

    context = {
        'errorMessage': errorMessageX,
        'errorMail': errorMail,
    }

    return HtmlTemplate.load('user_login/user_login.html').format(context)