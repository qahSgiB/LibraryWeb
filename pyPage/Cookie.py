from http.cookies import SimpleCookie



class Cookie():
    def __init__(self, name, value, attrs={}):
        self.name = name
        self.value = value
        self.attrs = attrs

    @staticmethod
    def loadFromHTTP(http):
        cookies = []

        cookieX = SimpleCookie(http)
        for name in cookieX.keys():
            cookies.append(Cookie(name, cookieX[name].value))

        return cookies

    def setExpirationTime(self, time):
        self.attrs['max-age'] = time

    def setExpirationTimeY(self, time):
        self.setExpirationTime(time*31536000)

    def setPath(self, path):
        self.attrs['path'] = path

    def setPathBase(self):
        self.setPath('/')

    def getHTTP(self):
        cookie = SimpleCookie()
        cookie[self.name] = self.value
        for attrName, attrValue in self.attrs.items():
            cookie[self.name][attrName] = attrValue

        http = cookie.output(header='', sep='')

        return http