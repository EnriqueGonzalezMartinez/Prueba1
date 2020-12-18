# Enrique Adrian Gonzalez Martinez
# programa que ingresa a un servidor udp con la ip y puerto indicada
# 24/10/2020  9:46 a.m.
import socket

direccion = ('127.0.0.1', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
    while True:
        mensaje = input("Cliente: ")
        cliente.sendto(mensaje.encode("utf-8"), direccion)
        if mensaje == "bye":
            break
        else:
            recibido = cliente.recvfrom(1024)
            mensaje2 = recibido[0].decode()
            ip = recibido[1]
            print("Servidor", ip, ":", mensaje2)