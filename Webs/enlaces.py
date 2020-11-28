# Enrique Adrian Gonzalez Martinez
# script que saca e imprime en pantalla los enlaces de una pagina web
# ‎14‎/10/‎2020, ‏‎10:26 a. m.

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.uanl.mx/enlinea'
re = requests.get(url)
soup = bs(re.content, 'html.parser')
links = soup.find_all('a', href=True)
for lab in links:
    print(lab)
address = [x['href'] for x in links]
for ad in address:
    print(ad)
