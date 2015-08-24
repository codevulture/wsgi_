##Sample wsgi server##


Wsgi gateway/server --> (invokes callable)Wsgi Application/Framework

web server: It returns a response to the client , doesn't create it.
web application: creates a response and sends to web server.
WSGI: Just a set of rules, this speecifies rules for web application and web
server so that they could communicate easily. After this they are called wsgi
compliant.

In WSGI architecture, WSGI Application has to be a callable and it needs to be
given to the Web Server, so the Web Server can call the Web Application
whenever the server recieves a request.
