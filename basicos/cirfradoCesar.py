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
modo = input("Ingrese el modo cifrar [1] descifrar [2]: ")

if modo == "1":
    cadena = input("Ingrse la cadena a cifrar: ")
    for i in cadena:
        if i != " ":
            posicion = alfabeto.index(i)
            if posicion + llave < len(alfabeto):
                cifrado += alfabeto[posicion + llave]
            else:
                cifrado += alfabeto[(posicion + llave) - len(alfabeto)]
        else:
            cifrado += " "
    print(cifrado)
elif modo == "2":
    cifrado = input("Ingrese la cadena a descifrar: ")
    for j in cifrado:
        if j != " ":
            posicion = alfabeto.index(j)
            descifrado += alfabeto[posicion - llave]
        else:
            descifrado += " "
    print(descifrado)
else:
    print("Esa no es una opcion.")
