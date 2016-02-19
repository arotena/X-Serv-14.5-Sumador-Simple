#!/usr/bin/python

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
primero = None;
try:
	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'HTTP request received:'
		get = recvSocket.recv(2048)
		numero = get.split()[1][1:]
		if primero != None:
			resultado = int(primero) + int(numero)
			primero = None
			res = "el resultado de tu suma es " + str(resultado)
		else:
			primero = numero
			res = "Dame otro numero"

		print  "numero " + str(numero)
		html = "<html><body>"
		html += "<p>" + res + "</p></html></body>"

		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
		                html + "\r\n")
		recvSocket.close()
except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()
