import time



def defaultLogHttpFuncFactory(logOnlyHtml=False, logCookies=False):
    def defaultLogHttpFunc(ip, path, status, headers, cookies):
        timeStr = time.ctime()
        contentType = headers['Content-type']

        log = True

        if logOnlyHtml:
            if contentType != 'text/html':
                log = False
        
        if log:
            print(f'[{timeStr}] | {ip} | {path} | {status} {contentType}')

        if logCookies:
            for cookie in cookies:
                print(f'\tSetting Cookie | {cookie.name}: {cookie.value} {cookie.attrs}\n')

    return defaultLogHttpFunc

def defaultLogFunc(message):
    timeStr = time.ctime()

    print(f'[{timeStr}] | {message}\n')



class Logger():
    def __init__(self, logHttpFunc=None, logFunc=None):
        if logHttpFunc == None:
            logHttpFunc = defaultLogHttpFuncFactory()
        if logFunc == None:
            logFunc = defaultLogFunc

        self.logHttpFunc = logHttpFunc
        self.logFunc = logFunc

    def logHttp(self, *args, **params):
        self.logHttpFunc(*args, **params)

    def log(self, *args, **params):
        self.logFunc(*args, **params)