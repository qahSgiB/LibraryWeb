#
#   How to run this
#       1. python main.py [https]
#           https - run http server inside ssl socket
#       2. In bowser open http://127.0.0.1:8080
#

def main():
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    import ssl
    import sys
    import time

    from pyPage.Server import Server
    from pyPage.Logger import Logger, defaultLogHttpFuncFactory

    from routes import htmlRoutes, errorRoutes


    useSSL = False

    if len(sys.argv) >= 2:
        useSSLCmd = sys.argv[1]
        if useSSLCmd == 'https':
            useSSL = True

    address = '192.168.1.4'
    port = 4434 if useSSL else 8080
    logOnlyHtml = True
    logCookies = True

    logger = Logger(defaultLogHttpFuncFactory(logOnlyHtml, logCookies))
    handlerFactory = Server.factory(htmlRoutes, errorRoutes, logger)

    with HTTPServer((address, port), handlerFactory) as httpServer:
        if useSSL:
            httpServer.socket = ssl.wrap_socket(httpServer.socket, certfile='./SSL/server.pem', server_side=True)

        serverTypeString = 'HTTPS' if useSSL else 'HTTP'
        logger.log(f'Started {serverTypeString} server on {address}:{port}\n\tLogging only text/html')
        
        try:
            httpServer.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
