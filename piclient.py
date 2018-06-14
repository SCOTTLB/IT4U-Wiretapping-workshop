#!/usr/bin/python
import socket,sys,time
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.42.1.61', 1337)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
message = "Heres the launch codes bob! 1234! Have a nice day :)\n"
while True:
    sock.sendall(message)
    time.sleep(1)
