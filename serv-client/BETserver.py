import socket

direccion = ('192.168.100.1', 10000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    print(f'Try to connected to {direccion}')
    servidor.connect(direccion)
    cmd = input('$: ')
    while cmd != 'exit':
        servidor.send(cmd.encode())
        resultado = servidor.recv(4096).decode()
        if resultado != '':
            print(resultado)
        cmd = input('$: ')
