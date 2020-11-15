import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.uanl.mx/enlinea'
re = requests.get(url)
soup = bs(re.content, 'html.parser')
images = soup.find_all('img', src=True)
imag = [x['src'] for x in images if x['src'].endswith('.jpg')]
for img in imag:
    last = img.rfind('/')
    img_name = img[last + 1:]
    with open("C:\\Users\\Adrian\\Pictures\\"+ img_name,'wb') as file:
        file.write(requests.get(img).content)
