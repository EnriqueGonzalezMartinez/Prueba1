import six

diccionario = dict()
opc = "Y"
while opc == "Y":
    clave = input("Clave: ")
    valor = input("Valor: ")
    diccionario[clave] = valor
    opc = input("Otro elemento? [Y] Si ")

for x,y in six.iteritems(diccionario):
    six.print_(x,y)
