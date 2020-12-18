import socket
import os
import subprocess

direccion = ('192.168.100.17', 10000)
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.bind(direccion)
    cliente.listen(4)
    print(f'Listen in port {direccion[1]}')
    client, addr = cliente.accept()
    print(f'Accept: {client}, address: {addr}')
    while True:
        cmd, addr = client.recvfrom(1024)
        cmd = cmd.decode()
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
                resultado = os.system('ls')
        elif cmd in ['rm','del']:
            cmd = cmd[cmd.find(' ')+1:]
            os.remove(cmd)
            resultado = f'Se elimino {cmd}'
        elif cmd == 'exit':
            break
        else:
            resultado = f'No se reconoce el comnado {cmd}'

        client.sendto(resultado.encode(), addr)
