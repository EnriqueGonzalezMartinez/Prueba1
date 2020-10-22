fila1 = ["a","b","c","d","e","f","g","h","i","j"]
fila2 = ["1","2","3","4","5","6","7","8","9"]
fila3 = []

for i in range(0,len(fila1)):
	fila3.append(fila1[i])
	if i < len(fila2):
                fila3.append(fila2[i])

print(fila3)

