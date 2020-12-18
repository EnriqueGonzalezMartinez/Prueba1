import re
import requests
from bs4 import BeautifulSoup as bs

def scraping(url,file):
    # Se lanza una peticion al sitio web y se saca su html
    try:
        req = requests.get(url)
        soup = bs(req.content, 'html.parser')
        # Expreciones para buscar informacion en las webs
        expreciones = [re.compile(r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}'), re.compile(r'facebook.com/\w*'), 
                    re.compile(r'twitter.com/\w*'), 
                    re.compile(r'\(\d{2}\)\d{4}-\d{4}|\(\d{2}\) \d{4} \d{4}|\(\d{2}\)\d{8}|\d{6}-\d{4}|\d{6} \d{4}')]
        data = []
        if (file == None):
            for exp in expreciones:
                # Se busca la informacion en el html de la web
                search = exp.findall(str(soup))
                for sh in search:
                    data.append(f'{sh}')
            if (data != []):
                for sh in data:
                    print(f'{sh}')
                print(f'El archivo {file} fue creado con exito.')
            else:
                print('No se encontro informacion en la web.')
        else:
            try:
                for exp in expreciones:
                    # Se busca la informacion en el html de la web
                    search = exp.findall(str(soup))
                    for sr in search:
                        data.append(sr)
                if (data != []):
                    with open(file,'w') as file2:
                        for sh in data:
                            file2.write(f'{sh}\n')
                    print(f'El archivo {file} fue creado con exito.')
                else:
                    print('No se encontro informacion en la web.')
            except:
                print('Error al crear el archivo, intente de nuevo.')
    except:
        print('La URL es incorrecta, intente de nuevo.')
