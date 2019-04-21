from a.sessionManager import checkSessionDecorator



emptyDecorator = lambda f: f

settings = {
    'isRedirect': False,
    'onViewDecorator': checkSessionDecorator,
    'onRedirectDecorator': checkSessionDecorator,
}

def getDefaultSettings():
    return dict(settings)