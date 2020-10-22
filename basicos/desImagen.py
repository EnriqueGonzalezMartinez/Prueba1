import urllib.request

url = "https://www.python.org/static/img/python-logo.png"
r = urllib.request.urlopen(url)

with open("imagen.png","wb") as file:
    file.write(r.read())