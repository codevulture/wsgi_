from wsgiref.simple_server import make_server

def app(first_argument,second_argument):
    "Web application which creates and returns response to the server."
    #To be wsgi compliant application must accept 2 arguments:
    #first containing information about the request.
    #first_argument = environment
    #print first_argument



    #second must be a callable: application must use this callable to notify
    #the server of the status of response and for setting various headers. This is
    #second condition for application to be WSGI.

    #second_argument = start_response
    second_argument('200 OK',[('Content-Length', '11')])

    body = "Successfull"

    #return must be an iterable , it could be string also but then it would
    #send it one by one character, so a list is preferable
    return [body]




httpd = make_server('',8111,app)
#wsgi server uses application as an argument.

httpd.serve_forever()
