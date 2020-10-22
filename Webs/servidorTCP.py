from cryptography.fernet import Fernet
import socket

TCP_IP = '127.0.0.1' 
TCP_PORT = 5005
BUFFER_SIZE = 2048 

# Aqui se crea el objeto socket del servidor de tipo TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor_tcp:
    # Se le asigna una IP y un puerto a el objeto socket con el metodo bind
    servidor_tcp.bind((TCP_IP,TCP_PORT))
    # Se le dice al objeto socket que esperamos 1 conexion de un cliente con el metodo listen 
    servidor_tcp.listen(1)
    # cliente es el objeto socket del cliente y addr es la IP del cliente
    # El metodo accept espera y acepta la conexion
    cliente, addr = servidor_tcp.accept()
    with cliente:
        while True:
            # La var mensaje recive lo que envia el cliente a travez del metodo
            # recv en bites, lo que esta entre paretesis es el limite de bites
            # que recibe y decodifica con decode
            mensaje = cliente.recv(BUFFER_SIZE)
            respuesta = "Enterado. Bye!"
            # Aqui al objeto socket del cliente se le envia la respuesta que esta
            # en la var respuesta con el metodo send y se codifica con el metodo
            # encode en formato utf-8
            cliente.send(respuesta.encode("utf-8"))
            break

# Se abre el archivo clave.key y se le asigna su contenido a la var key
with open("clave.key","rb") as file:
    key = file.read()
# Se crea el objeto de cifrado con la llave key
objeto = Fernet(key)
# Se desencripta el mensaje y se guarda en la var new
new = objeto.decrypt(mensaje)
print(new.decode())