import socket
import sys

direccion = ('127.0.0.1', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    try:
        servidor.bind(direccion)
    except:
        print("Bind filed")
        sys.exit()
    print("Socket bind success")
    servidor.listen(3)
    print("Socket is listening")
    while 1:
        conn, addr = servidor.accept()
        print("Connect with", addr[0], ":" + str(addr[1]))
        buf = conn.recv(1024).decode()
        print(buf)
     