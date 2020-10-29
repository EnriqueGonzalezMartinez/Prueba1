import socket
import os

direccion = ('127.0.0.1', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind(direccion)
    servidor.listen(1)
    cliente, adrr = servidor.accept()
    with cliente:
        while True:
            comando = cliente.recvfrom(2048)
            stream = os.popen(comando[0].decode("utf-8"))
            salida = stream.read()
            if salida.encode() == b'':
                cliente.sendto(b'null', direccion)
            else:
                cliente.sendto(salida.encode("utf-8"), direccion)
