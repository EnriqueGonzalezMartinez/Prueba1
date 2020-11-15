import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.uanl.mx/enlinea'
re = requests.get(url)
soup = bs(re.content, 'html.parser')
images = soup.find_all('img', src=True)
for img in images:
    print(img)
imag = [x['src'] for x in images if x['src'].endswith('.jpg')]
for img in imag:
    print(img)
