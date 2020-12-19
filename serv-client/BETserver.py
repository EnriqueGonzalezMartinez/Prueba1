import socket

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
            resultado = cliente.recv(4096).decode()
            print(resultado)
        cmd = input('$: ')

