import re

exprecion_fecha = re.compile(r'(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic) ( \d|\d{2})')
exprecion_hora = re.compile(r'\d{2}:\d{2}:\d{2}')
exprecion_usuario = re.compile(r'user \w*')
x = 0

with open("/var/log/auth.log","r") as file:
    for line in file:
        if x > 10:
            break
        mo1 = exprecion_fecha.search(line)
        mo2 = exprecion_hora.search(line)
        mo3 = exprecion_usuario.search(line)
        print("Fecha: ",mo1.group())
        print("Hora: ",mo2.group())
        try:
            print("Usr: ",mo3.group())
        except:
            print("Usr: none")
        x += 1
