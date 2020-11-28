import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Se ingersan los datos requeridos
msg = MIMEMultipart()
correo = input('Correo remitente: ')
# Verifica que el correo contenga un @
while correo.find('@') < 0:
    correo = input('Correo remitente: ')

msg['From'] = correo
password = input('Contraseña: ') 
# Asegura que el password tenga al menos un caracter
while len(password) <= 0:
    password = input('Contraseña: ')
# Se verifica que el correo tenga un @
correo2 = input('Correo destinatario: ')
while correo2.find('@') < 0:
    correo2 = input('Correo destinatario: ')

msg['To'] = correo2
msg['Subject'] = input('Asunto del correo: ')
cuerpo = input('Cuerpo del correo: ')
msg.attach(MIMEText(cuerpo))

# Se pide la ruta de la imagen y se adjunta al correo
path = input('Ruta de la imagen: ')
while not os.path.isfile(path):
    path = input('Ruta de la imagen: ')
# Se saca el nombre de la imagen
nombre = path[path.rfind('/') + 1:]

with open(path,'rb') as file:
    image = MIMEImage(file.read())
    image.add_header('Content-Disposition', f'attachment; filename = {nombre}')
    msg.attach(image)
# Se crea el contexto y se pide la opcion de envio
context = ssl.create_default_context()
opcion = input('Opcion de envio SSL[1] TLS[2]: ')

if(opcion == '1'):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
        try:
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print(f'Correo enviado a {msg["To"]} con exito.')
        except:
            print('El correo o contraseña son incorrectos')
elif(opcion == '2'):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        try:
            server.starttls(context=context)
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print(f'Correo enviado a {msg["To"]} con exito.')
        except:
            print('El correo o contraseña son incorrectos')
else:
    print('Esa no es una opcion.')
