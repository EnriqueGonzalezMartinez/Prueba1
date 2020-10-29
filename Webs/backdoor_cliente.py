import socket

direccion = ('127.0.0.1', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(direccion)
    while True:
        comando = input("Comando: ")
        if comando == "exit":
            break
        cliente.sendto(comando.encode("utf-8"), direccion)
        respuesta = cliente.recvfrom(2048)
        print("Respuesta:",respuesta[0].decode("utf-8"))
