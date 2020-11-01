import hashlib

#print(hashlib.algorithms_available)

texto = "hola"
md5_texto = hashlib.md5(texto.encode())
print(md5_texto.hexdigest())

sha1_texto = hashlib.sha1(texto.encode())
print(sha1_texto.hexdigest())

sha256_txt = hashlib.sha256(texto.encode())
print(sha256_txt.hexdigest())

sha512_txt = hashlib.sha512(texto.encode())
print(sha512_txt.hexdigest())
