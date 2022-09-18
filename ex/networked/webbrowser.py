# This is a simple web browser!
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# below is where connexion is made, can blow up if didnt connect to the host and port
# extend the socket and connect to this webserver data.p4re.org, port 80, there has to be some software runningin the host
mysock.connect(('data.pr4e.org', 80))

# http protocol
# whether the web server says hello or not is up to the application protocol, in this case we need to speak first as we are the web browser
# sends request to web server and web server processes the request and sends us back some data
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    # request 112 characters each time, can be specified
    data = mysock.recv(112)
    if (len(data) < 1):
        break
    print('line', data.decode(), end='\n---\n')
mysock.close()