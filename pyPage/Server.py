from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler
from pathlib import Path
import importlib.util

from pyPage.DecodeData import decodeData



class Server(BaseHTTPRequestHandler):
    def __init__(self, routes, errorRoutes, *args, **params):
        self.routes = routes
        self.errorRoutes = errorRoutes

        self.handleAsPublic = ['css', 'js', 'jpg', 'jpeg', 'png']
        self.publicContentTypes = {
            'css': ['text', 'css'],
            'js': ['text', 'javascript'],
            'jpg': ['image', 'jpg'],
            'jpeg': ['image', 'jpeg'],
            'png': ['image', 'png'],
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

    def sendHeaders(self, status, headers):
        self.send_response(status)

        for headerName, headerValue in headers.items():
            self.send_header(headerName, headerValue)

        self.end_headers()

    def sendContent(self, content, encoding='UTF-8'):
        self.wfile.write(bytes(content, encoding))

    def send(self, content, status, headers, encoding='UTF-8'):
        self.sendHeaders(status, headers)
        self.sendContent(content, encoding)

    def handleGet(self, path, postData=None):
        pathString = path

        pathStringSplitted = pathString.split('?')

        path = pathStringSplitted[0]
        getData = None

        if len(pathStringSplitted) > 1:
            getDataString = pathStringSplitted[1]
            getData = decodeData(getDataString)

        extension = None

        splittedPath = path.split('.')
        if len(splittedPath) == 1:
            extension = 'html'
        else:
            extension = splittedPath[-1]

        if extension == 'html':
            content, status, headers, error = self.handleHtml(path, getData, postData)
            if error is not None:
                errorContentPath = Path('page/html'+self.errorRoutes[error])
                with open(errorContentPath, 'r') as contentFile:
                    content = contentFile.read()

            self.send(content, status, headers)
        elif extension in self.handleAsPublic:
            content, status, headers, error = self.handlePublic(path, extension)

            if error is not None:
                content = ''
                headers['Content-type'] = 'text/plain'

            self.send(content, status, headers)

    def handlePublic(self, path, extension):
        content = None
        error = None
        status = 200
        contentType = self.publicContentTypes[extension]
        headers = {'Content-type': '/'.join(contentType)}

        if extension == 'css':
            headers['Content-type'] = 'text/css'

        route = path
        contentPath = Path(f'page/public/{extension}{route}')

        if contentPath.is_file():
            readMethod = None
            if contentType[0] == 'text':
                readMethod = 'r'
            else:
                readMethod = 'rb'

            with open(contentPath, readMethod) as contentFile:
                content = contentFile.read()
        else:
            error = 'not_found'
            status = 404

        return content, status, headers, error

    def handleHtml(self, path, getData, postData):
        content = None
        error = None
        status = 200
        headers = {'Content-type': 'text/html'}

        if path in list(self.routes.keys()):
            route = self.routes[path]
            contentPath = Path('page/html'+route)

            if contentPath.is_file():
                extension = route.split('.')[1]
                if extension == 'html':
                    with open(contentPath, 'r') as contentFile:
                        content = contentFile.read()
                elif extension == 'py':
                    spec = importlib.util.spec_from_file_location('pyHtml', contentPath)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    content = module.render(getData, postData)
            else:
                error = 'not_found'
                status = 404
        else:
            error = 'not_found'
            status = 404

        return content, status, headers, error

    def factory(*fargs):
        return lambda *args, **params: Server(*fargs, *args, **params)
