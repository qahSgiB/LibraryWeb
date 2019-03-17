import socketserver

from pyPage.Server import Server

from routes import htmlRoutes, errorRoutes



def main():
    address = '127.0.0.1'
    port = 8080
    handlerFactory = Server.factory(htmlRoutes, errorRoutes)

    with socketserver.TCPServer((address, port), handlerFactory) as httpServer:
        try:
            print(f'HTTP server on ({address}:{port})')
            httpServer.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
