import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

port = 587  # For SSL
password = "pc.test#1234"
# Se crea el objeto MIME donde se guardan las partes del correo
msg = MIMEMultipart()
msg['From'] = "test2.fcfm.pc@gmail.com"
msg['To'] = "adriangzz2001@gmail.com"
msg['Subject'] = "Prueba #2"
msg.attach(MIMEText("Esta es una prueba."))
print('Correo creado com exito')
# Se abre la imagen y se adjunta al objeto MIME
with open('C:/Users/Adrian/OneDrive - uanl.edu.mx/Pictures/piramide.JPG','rb') as file:
    image = MIMEImage(file.read())
    image.add_header('Content-Disposition', 'attachment; filename = "Imagen"')
    msg.attach(image)

print('Imagen adjuntada con exito')
# Se crea un contexto 
context = ssl.create_default_context()
# Se envia el correo con el contenido del objeto MIME
with smtplib.SMTP("smtp.gmail.com", port) as server:
    server.starttls(context=context)
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())

print('Correo enviado con exito')