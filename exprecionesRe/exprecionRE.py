import re
"""
 Caracteres predefinidos

\d  Cualquier carácter que sea dígito
\D  Cualquier carácter que no sea dígito
\w  Cualquier carácter alfanumérico
\W  Cualquier carácter no alfanumérico
\s  Espacio en blanco
\S  Cualquier carácter que no sea espacio

 Caracteres que permiten repeticiones

+  El carácter de la izquierda aparecerá una o varias veces
*  El carácter de la izquierda aparecerá cero o más veces
?  El carácter de la izquierda aparecerá cero o una vez
{}  Indica el número de veces que debe aparecer el carácter de la izquierda:

exprecion_telefono = re.compile(r'\(\d\d\)\d\d\d\d-\d\d\d\d')

exprecion_telefono = re.compile(r'\(\d\d\)\d{4}-\d{4}|\(81\)\d{4} \d{4}')

exprecion_telefono = re.compile(r'\(\d\d\)\d{4}-\d{4}|\(81\)\d{4} \d{4}|\(81\)\d{8}|81\d{4}-\d{4}|81\d{4} \d{4}|81\d{8}')

mo = exprecion_telefono.search(input("Su telefono: "))

try:
    print(mo.group())
except:
    print("Error perron")

exprecion_correo = re.compile(r'\w*.\w*@uanl.edu.mx')
mo = exprecion_correo.findall("juanito.gutierritos@uanl.edu.mx")
correo = mo[0]
posicion1 = correo.find(".")#Posicion donde termina el nombre
posicion2 = correo.find("@")#Posicion donde termina el apellido
nombre = []
apellido = []
nombre = nombre + [correo[ : posicion1]]
apellido = apellido + [correo[posicion1 + 1 : posicion2]]

try:
    print(nombre)
    print(apellido)
except:
    print("error")
"""
meses = "Enero|Febrero|Marzo|Abril|Mayo|Junio|Julio|Agosto|Septiembre|Octubre|Noviembre|Diciembre"
meses_abrebiados = "Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic"
exprecion_fecha = re.compile(r'(%s|%s) \d*' %(meses, meses_abrebiados))
exprecion_hora = re.compile(r'\d{2}:\d{2}:\d{2}')
exprecion_usuario = re.compile(r'user \w*')

mo = exprecion_fecha.search("asdfasdf   Feb 27")
mo2 = exprecion_hora.search("01:13:32")
mo3 = exprecion_usuario.search("user root")

print(mo.group())
print(mo2.group())
print(mo3.group())
















