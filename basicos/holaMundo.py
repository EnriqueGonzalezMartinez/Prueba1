import time, os, requests
"""
file = open("Hola Mundo.txt","w")
file.write("Hola Mundo!\n")
file.close()

with open("Hola Mundo.txt","r") as file:
    for line in file:
        print(line)
        
path = "/home/adrian/holaMundo.txt"

with open(path,"r+") as file:
    file.write("Buenas tardes!!!!")
    for line in file:
        print(line)
"""
name = "/urls.txt"
ruta = os.path.abspath("")
print(ruta)
with open(ruta+name, "w") as file:
    with open(ruta+"/urls2.txt","w") as file2:
        line = 2
        count = 1
        url = "buenas.com"
        for line in file:
            if line == count:
                file2.write(url)
            else:
                file2.write(line)
        count += 1
remove("urls.txt")

with open(ruta+"/urls2.txt", "r") as file:
    print(file.read())

    
        

    
    

