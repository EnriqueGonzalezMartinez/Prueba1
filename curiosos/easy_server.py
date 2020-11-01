# servidor "dummy" para simular autenticacion
# @author: Romeo Sánchez (2020)

import socket
import os
import hashlib

users = {
    "admin": "8621ffdbc5698829397d97767ac13db3",
    "scott": "5f4dcc3b5aa765d61d8327deb882cf99", 
    "dummy": "eb0a191797624dd3a48fa681d3061212", 
    "romeo": "2dccd1ab3e03990aea77359831c85ca2",
    "root" : "5d41402abc4b2a76b9719d911017c592"
}

host = 'localhost'
port = 1337
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))
sock.listen(10)
print("Easy server. Hack me, if you can!")

while(True):
    print("Esperando una conexión...")
    cli, addr = sock.accept() 

    # un cliente se conecta
    print("Conexión recibida desde ", addr)
    
    while(True):

        # protocolo
        # intenta autenticar al usuario remoto

        # recibe username
        usuario = cli.recv(1024).decode()
        print(f"Usuario recibido: {usuario}")

        # envía respuesta
        cli.send("Escriba el password:".encode())

        # recibe password
        password = cli.recv(1024).decode()
        # los passwords son invisibles, nunca deben imprimirse :)
        print("Password recibido: *****")

        # verifica la existencia de las credenciales
        if usuario in users:

            # calcula el hash del password
            pw = hashlib.md5(password.encode())
            pwHash = pw.hexdigest()

            # si el hash recibido es igual al hash guardado,
            # el usuario tiene acceso
            if pwHash == users[usuario]:
                cli.send("Ok".encode())
                break
            else:
                cli.send("Acceso denegado".encode())
                cli.close()
                break


