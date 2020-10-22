import requests, time
from bs4 import BeautifulSoup as bs

response = requests.get("https://es.wikipedia.org/wiki/Naruto")
soup = bs(response.content,"html.parser")
print(response)
print(soup)
    
"""
with open("/home/adrian/Escritorio/Urls/urls.txt") as file:
    x = 0
    for url in file:
        page = requests.get(url, headers={"user-agent" : "Mozilla/5.0"})
        if page.status_code == 200:
            x += 1
        time.sleep(2)
print(x)

url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
# Download the page.
print('Downloading page %s...' % url)
res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, "html.parser")
comicElem = soup.select('#comic img')
if comicElem == []:
    print('No se encontró.')
else:
    comicUrl = comicElem[0].get('src')
    print('Descargando %s...' % (comicUrl))
    response = requests.get('http:'+comicUrl)
    if response.status_code == 200:
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in response.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

print('Hecho.')
"""
