maximo = 0
pila = []
cima = 0

def llenar(pila, maximo):
	for elemento in range(0,maximo):
		pila += [""]

def apilar(elemento):
	global maximo
	global cima
	global pila

	if cima < maximo:
		pila[cima] = elemento
		cima += 1

def desapilar():
        global maximo
        global cima
        global pila
        
        if cima > 0:
                print("Desapilando: ",pila[cima-1])
                pila[cima - 1] = ""
                cima -= 1

def mostrar():
	global maximo
	global cima
	global pila

	for posicion in range(maximo - 1,-1,-1):
		print(pila[posicion])

maximo = int(input("Limite maximo: "))
llenar(pila, maximo)
for elemento in range(0, maximo):
	apilar(input("Elemento a apilar: "))
	mostrar()
	
desapilar()
mostrar()
