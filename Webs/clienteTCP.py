import argparse
import socket
from cryptography.fernet import Fernet

def clienteTCP(TCP_IP, TCP_PORT, BUFFER_SIZE):
    # Aqui se declara el argumento -msj
    description = """ Modo de uso:programa.py -msg "Mensaje a Enviar"""            
    parser = argparse.ArgumentParser(description="Escaneo de puerto",
                                    epilog=description,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-msj", metavar="MSJ", dest="msj",
                        help="mensaje a enviar", required=True)
    params = parser.parse_args()
    # Se genera la key y el objeto de cifrado
    key = Fernet.generate_key()
    objeto = Fernet(key)
    # Se crea el archivo clave.key donde se guarda la llave en bites
    with open("clave.key","wb") as file:
        file.write(key)
    # Se le da el valor del parametro msj a la var mensaje
    mensaje = params.msj
    # Primero se codifica la var mensaje en formato utf-8 y despues se encripta
    # y se guada en la var cryp_msj
    cryp_msj = objeto.encrypt(mensaje.encode("utf-8"))
    print(cryp_msj)
    # Se crea el objeto socket del cliente tipo TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_tcp:
        # Se conecta a la IP y pueto en la tupla con el metodo connect
        cliente_tcp.connect((TCP_IP,TCP_PORT))
        # Se envia el mensaje en la var cryp_msj codificado en utf-8
        cliente_tcp.send(cryp_msj)
        # En la var recivir se guarda el mensaje del servidor 
        # y se decodifica con el metodo decode
        recivir = cliente_tcp.recv(BUFFER_SIZE).decode()
        print(recivir)

TCP_IP = '127.0.0.1' 
TCP_PORT = 5005
BUFFER_SIZE = 2048
clienteTCP(TCP_IP, TCP_PORT, BUFFER_SIZE)
