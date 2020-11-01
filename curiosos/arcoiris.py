# Enrique Adrian Gonzalez Martinez
# script que crea dos archivos con el hash md5 y sha256 
# de las contraseñas del documento 100password.txt 
# 31/10/2020 11:05 a.m.
import hashlib

archivo = "100passwordsMD5.txt"
contras = open("100passwords.txt",'r',errors='ignore').readlines()
contras = list(map(str.strip, contras))
hashes_md5 = []
hashes_sha256 = []
for contra in contras:
    md5 = hashlib.md5(contra.encode())
    resum = md5.hexdigest()
    hashes_md5.append(resum)
    sha256 = hashlib.sha256(contra.encode())
    hashes_sha256.append(sha256.hexdigest())

with open(archivo, 'w') as file:
    for i in range(len(contras)):
        file.write(f'{hashes_md5[i]}\t{contras[i]}\n')

with open("100passwordsSHA256.txt", 'w') as file:
    for j in range(len(contras)):
        file.write(f'{hashes_sha256[j]}\t{contras[j]}\n')

print(f"Archivo: {archivo} creado")
print("Archivo: 100passwordsSHA256.txt creado")
