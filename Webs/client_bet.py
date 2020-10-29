import socket
import sys

direccion = ('192.168.100.17', 2000)
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(direccion) #IP is the server IP
 
for args in sys.argv:
    if args == "":
        args = 'no args'
    else:
        s.send(args.encode())
 
print ('goodbye!')