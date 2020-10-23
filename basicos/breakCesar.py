# Enrique Adrian Gonzalez Martinez
# programa que rompe el cifrado de una cadena pedida al usuario
# por defaul esta la cadena "dwdtxhq do dpdqhfhu"
# 17/10/2020-‏‎01:44 p.m.

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z",
            "1","2","3","4","5","6","7","8","9","0","A","B","C",
            "D","E","F","G","H","I","J","K","L","M","N","O","P",
            "Q","R","S","T","U","V","W","X","Y","Z",]
llave = 3
# Variable que guarda la cadena que se cifrara
cadena = ""
# Variable que guarda la cadena ya cifrada
cifrado = ""
# Variable que guarda la cadena ya descifrada
descifrado = ""
# Variable que guarda la posicion que tiene un simbolo de la cadena en el alfabeto
posicion = 0

cadena = input("Ingrese la cadena a cifrar: ")
if len(cadena) == 0:
    cadena =  "dwdtxhq do dpdqhfhu"
for i in cadena:
        if i != " ":
            posicion = alfabeto.index(i)
            if posicion + llave < len(alfabeto):
                cifrado += alfabeto[posicion + llave]
            else:
                cifrado += alfabeto[(posicion + llave) - len(alfabeto)]
        else:
            cifrado += " "

for x in range(len(alfabeto)):
    llave = x
    for j in cifrado:
        if j != " ":
            posicion = alfabeto.index(j)
            descifrado += alfabeto[posicion - llave]
        else:
            descifrado += " "
    print("Llave #",llave,": ",descifrado)
    descifrado = ""
