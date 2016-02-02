from wsgiref.simple_server import make_server

def Application(environment, start_response):
    headers = [('Content-Length','8')]
    start_response('200 OK', headers)
    body = 'Length=8'
    return [body]



httpd = make_server('', 8051, Application)
httpd.serve_forever()

