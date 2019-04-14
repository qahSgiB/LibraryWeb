from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler
from pathlib import Path
import importlib.util

from pyPage.DecodeData import decodeData
from pyPage.Template import HtmlTemplate, PyTemplate
from pyPage.Cookie import Cookie



class Server(BaseHTTPRequestHandler):
    def __init__(self, routes, errorRoutes, *args, **params):
        self.routes = routes
        self.errorRoutes = errorRoutes

        self.handleAsPublic = ['css', 'js', 'jpg', 'jpeg', 'png', 'ico']
        self.publicContentTypes = {
            'css': ['text', 'css'],
            'js': ['text', 'javascript'],
            'jpg': ['image', 'jpg'],
            'jpeg': ['image', 'jpeg'],
            'png': ['image', 'png'],
            'ico': ['image', 'ico'], # ??
        }

        super().__init__(*args, **params)

    def do_POST(self):
        postData = self.getPostData()

        self.handleGet(self.path, postData)

    def do_GET(self):
        self.handleGet(self.path)

    def getPostData(self):
        contentLength = int(self.headers['Content-Length'])
        postDataString = self.rfile.read(contentLength).decode("utf-8")

        return decodeData(postDataString)

    def getCookies(self):
        cookiesHTTP = self.headers['Cookie']
        cookies = Cookie.loadFromHTTP(cookiesHTTP)

        return cookies

    def sendHeaders(self, status, headers, cookies):
        self.send_response(status)

        for headerName, headerValue in headers.items():
            self.send_header(headerName, headerValue)

        for cookie in cookies:
            self.send_header('Set-cookie', cookie.getHTTP())

        self.end_headers()

    def sendContent(self, content, encoding, isBytes):
        if not isBytes:
            content = bytes(content, encoding)

        self.wfile.write(content)

    def send(self, content, status, headers, cookies, encoding='UTF-8', isBytes=False):
        self.sendHeaders(status, headers, cookies)
        self.sendContent(content, encoding, isBytes)

    def handleGet(self, path, postData=None):
        pathString = path

        pathStringSplitted = pathString.split('?')
        path = pathStringSplitted[0]

        getData = None

        if len(pathStringSplitted) > 1:
            getDataString = pathStringSplitted[1]
            getData = decodeData(getDataString)

        cookies = self.getCookies()

        extension = None

        splittedPath = path.split('.')
        if len(splittedPath) == 1:
            extension = 'html'
        else:
            extension = splittedPath[-1]

        if extension == 'html':
            content, status, headers, sendCookies, error = self.handleHtml(path, getData, postData, cookies)
            if error is not None:
                errorContentPath = Path('page/htmlTemplates'+self.errorRoutes[error])
                with open(errorContentPath, 'r') as contentFile:
                    content = contentFile.read()

            self.send(content, status, headers, sendCookies)
        elif extension in self.handleAsPublic:
            content, status, headers, error, isBytes = self.handlePublic(path, extension)

            if error is not None:
                content = ''
                headers['Content-type'] = 'text/plain'

            self.send(content, status, headers, [], isBytes=isBytes)

    def handlePublic(self, path, extension):
        content = None
        error = None
        status = 200
        contentType = self.publicContentTypes[extension]
        headers = {'Content-type': '/'.join(contentType)}
        isBytes = False

        route = path
        contentPath = Path(f'page/public/{route}')

        if contentPath.is_file():
            readMethod = None
            if contentType[0] == 'text':
                readMethod = 'r'
            else:
                readMethod = 'rb'
                isBytes = True

            with open(contentPath, readMethod) as contentFile:
                content = contentFile.read()
        else:
            error = 'not_found'
            status = 404

        return content, status, headers, error, isBytes

    def handleHtml(self, path, getData, postData, cookies):
        content = None
        error = None
        status = 200
        headers = {'Content-type': 'text/html'}

        if path in list(self.routes.keys()):
            route = self.routes[path]
            contentPath = 'page/views'+route

            if Path(contentPath).is_file():
                spec = importlib.util.spec_from_file_location('page/views', contentPath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                content, cookies = module.view(getData, postData, cookies)
            else:
                error = 'not_found'
                status = 404
        else:
            error = 'not_found'
            status = 404

        return content, status, headers, cookies, error

    @staticmethod
    def factory(*fargs):
        return lambda *args, **params: Server(*fargs, *args, **params)
