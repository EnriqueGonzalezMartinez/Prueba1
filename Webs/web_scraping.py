import shutil, os, time, json, requests, re
from openpyxl import Workbook
from bs4 import BeautifulSoup as bs

def urls(busqueda, page):
    search = "https://www.google.com/search?q=%s" %busqueda
    #saca las urls de la pagina de google
    pag = int(page+"0")
    urls = []
    for i in range(0,pag,10):
        response = requests.get(search+"&start=%d" %i)
        soup = bs(response.content,"html.parser")
        links = soup.find_all('a')
        for indice in range(0,len(links)):
            link = links[indice]['href']
            inicio = link.find('http')
            if inicio != -1:
                urls.append(link[inicio:])
    print("Buscando paginas web.....")
    time.sleep(4)
    #crea la ruta absoluta a la carpeta Urls y guarda los docs.txt con las urls
    os.makedirs("Urls", exist_ok=True)
    ruta = os.path.abspath("Urls")
    with open(ruta+"/urls.txt","w") as file:
        for url in urls:
            if url.find("google") == -1:
                indice = url.find("&")
                file.write(url[:indice]+"\n")
    print("Hecho")
    time.sleep(3)
    
def Menu(ruta):
    global archivoUrl
    os.system("cls")
    print("Con qué archivo le gustaría trabajar?")
    num = 1
    directorio = os.listdir(ruta)
    for archivo in directorio:
        print(num,")", archivo)
        num += 1
    opc = int(input("\nIngrese el número del archivo que desea tratar: ")) - 1
    print(len(directorio))
    while opc >= len(directorio):
        opc = int(input("\nIngrese un número valido: ")) - 1
    rutaArch = os.path.join(ruta,directorio[opc])
    archivoUrl = directorio[opc]
            
    while True:
        os.system("cls")
        print("¿Qué desea hacer con el archivo?")
        print("---------Menu---------\n1) Leer\n2) Agregar\n3) Actualizar\n4) Salir\n-----------------------")
        x= int(input("Ingresa un numero: "))
        print("-----------------------")
        while type(x) != int:
            x = int(input("Por favor ingrese un número: "))
            
        if x == 1:
            os.system("cls")
            archivo = open(rutaArch,"r")
            print(archivo.read())
            input("\nPresione enter para continuar: ")
            os.system("cls")
            archivo.close()
            continue
            
        if x == 2:
            os.system("cls")
            nuevaLinea = str(input("Ingrese el url a agregar: "))
            regex = re.compile(r'https://www') #expresion regular
            direccion_url =regex.search(nuevaLinea) 
            if direccion_url==None: 
                print ("Link incorrecto")
            else:
                archivo = open(rutaArch,"a")
                archivo.write(nuevaLinea)
                archivo.close()
                print("El link fue añadido")
            time.sleep(2)
            continue
        if x == 3:
            archivo=open(rutaArch, "r")
            archivo.seek(0) #rewind
            print(archivo.read())
            archivo.close()
            input("\nPresione enter para continuar: ")
            continue
        
        if x == 4:
            return False

        else:
            os.system("cls")
            input("Ingrese un valor valido, presione enter para continuar: ")

def descargarWeb(archivo,ruta):
    os.system("cls")
    #se crea la ruta absoluta a la carpeta Urls
    #ruta = os.path.abspath("Urls")
    #ruta para crear la carpeta PagWebs dentro de la carpeta Urls
    ruta_abs = ruta + "/PagWebs"
    #Se crea la carpeta PagWebs donde se guardaran los archivos.txt
    os.makedirs(ruta_abs, exist_ok=True)
    #Se descargan las paginas y se guarda la informacion en archivos.txt
    ruta_archivo = ruta +"/"+ archivo
    with open(ruta_archivo,"r") as file:
        num = 1
        for line in file:
            Agente = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
            page = requests.get(line, headers={"user-agent":Agente})
            #if page.status_code != 200:
                #continue
            #Se crea el nombre de archivo.txt
            name = "/PG%d.txt" %num
            with open(ruta_abs+name,"wb") as file2:
                file2.write(page.content)
            print("Descargando paginas web...")
            num += 1
            time.sleep(2)
    print("Hecho")

def infoSig(ruta):
    informacion = [[],[],[],[],[]]
    files_pagwebs = os.listdir(ruta)
    files_pagwebs.sort()
    #expreciones regulares que buscan fecha, correo, telefono, facebook, tweeter, instagram
    mes = "Enero|Febrero|Marzo|Abril|Mayo|Junio|Julio|Agosto|Septiembre|Octubre|Noviembre|Diciembre"
    mes_abr = "Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic"
    exp1 = re.compile(r'(\d*) (%s|%s) (\d*)|(%s|%s) (\d*)( \d*)|(\d*) de (%s|%s)( de)?( \d*)?' %(mes, mes_abr,mes, mes_abr,mes, mes_abr), re.I)
    exp2 = re.compile(r'\w*@\w*.com(.mx)?')
    exp3 = re.compile(r'\(\d{2}\)\d{4}-\d{4}|\(\d{2}\) \d{4} \d{4}|\(\d{2}\)\d{8}|\d{6}-\d{4}|\d{6} \d{4}')
    exp4 = re.compile(r'facebook.com/\w*')
    exp5 = re.compile(r'twitter.com/\w*')
    exp6 = re.compile(r'instagram.com/\w*')
    lista = [exp2,exp3,exp4,exp5,exp6]
    for file in files_pagwebs:
        ruta_abs = ruta + file
        #abre el archivo con el codigo de la pagina
        with open(ruta_abs,"rb") as file:
            soup = bs(file,"html.parser")
            #agrega a la lista los str que coincidan con los patrones
            for i in range(len(lista)):
                info = lista[i].search(str(soup))
                try:
                    informacion[i].append(info.group())
                except:
                    informacion[i].append("Info no encontrada")

    return informacion

def clima():
    while True:
        os.system("cls")
        print( "¿Desea revisar el clima de alguna ciudad?\n 1) Si\n 2) No")
        try:
            opc_clima=int(input("Ingrese un número: "))
        except:
            print("Caracter no válido, vuelva a intentarlo")
            input("\nPresione enter para continuar:")
            continue
        os.system("cls")
        if opc_clima==1:
            api_url = "http://api.openweathermap.org/data/2.5/weather?appid=029b8a2a494a487162a13e7adec9e027&q="
            city = input("Ingrese la ciudad del congreso: ")
            no_valido=re.compile(r"\s+")
            mo=no_valido.search(city)
            if city != mo:
                url= api_url + city
                json_data = requests.get(url).json()
                if json_data["cod"] != "404":
                    formatted_data = json_data["weather"][0]["main"]
                    print("Weather: " + formatted_data)
                          
                    formatted_data = json_data["weather"][0]["description"]
                    print("Weather description: " + formatted_data)
                                             
                    formatted_data = json_data["main"]["temp"]
                    celsius = int(formatted_data) - 273.15
                    print("Temperature: " + str(celsius) + "°")
            
                    formatted_data = json_data["main"]["humidity"]
                    print("Humidity: " + str(formatted_data) + "%")
                    time.sleep(1)
                    input("\nPresione enter para continuar:")
                    continue
                else:
                    print("Ciudad no encontrada")
                    input("\nPresione enter para continuar:")
                    continue
            else:
                print("Vuelva a intentarlo")

        elif opc_clima==2:
            break


rutaDesk = str(input("Ingrese la ruta donde se encuetra la carpeta PIA IP \nParecido a este formato: C:/Users/(User)/Desktop (No incluya la ultima diagonal \"/\")\n"))
ruta = rutaDesk + "/PIA IP/Urls"
webs = urls("congreso de ciberseguridad 2020","2")
os.system("cls")

Menu(ruta)

descargarWeb("urls.txt",ruta)
os.system("cls")

clima()

print("Se está creando el archivo excel: ")
#Ruta hacia la carpeta donde estan los archivos de las paginas        
lista=(infoSig( ruta + "/PagWebs/"))
#de la lista se extrajó la lista de Correo,Telefono,Facebook,Twitter e Instagram para luego usarla al momento de crear el documento excel
Correo=lista[0]
Telefono=lista[1]
Facebook=lista[2]
Twitter=lista[3]
Instagram=lista[4]

#crear archivo excel con datos de los congresos
libro= Workbook()
pagina=libro.active

pagina['A1']='Conferencia'
pagina['B1']= 'Lugar'
pagina['C1']= 'Fecha'
pagina['D1']='Correo Electrónico'
pagina['E1']='Teléfono'
pagina['F1']='Facebook'
pagina['G1']='Twitter'
pagina['H1']='Instagram'
pagina['I1']='Clima'

Nombre=["infosecurity","congreso de ciberseguridad e inteligencia","Infosecurity México 2020","IV congreso de informática forense y ciberseguridad 2020","CISO DAY 2020","Cloud & Cyber Security Expo Madrid","Congreso de informática forense y ciberseguridad 2020","Tactical Edge Virtual Summit","The Future of Cyber Security Virtual","XIV Congreso Internacional de Ciberseguridad Industrial","ASLAN 2020","c0r0n4con","IT Masters Forum","Teletrabajo seguro para tu empresa","SECURITY FORUM","Congreso Internacional de Ciberseguridad","Marco de referencia para la gestión de datos","XII Encuentro de la Seguridad Integral","Congreso Cybersecurity Bank & Government Buenos Aires, Argentina 2020","ASLAN 2021"]
Lugares=["Centro Citibanamex"," ","Centro Citibanamex","Hotel Paradisus Punta Cana, Rep. Dominicana","Madrid","Madrid","Madrid"," ","Virtual","Ciudad de México","Palacio de Congresos de Madrid","Virtual"," Dream Vista, Cancún","Virtual","Barcelona","Panamá","Ciudad de México","virtual","Hotel 725 Continental, Buenos Aires","Madrid"]
Fecha=["2020-09-22","2019-10-03","2020-09-22","2020-08-06","2020-06-09","2020-10-28","2020-03-31","2020-08-11","2020-06-09","cancelado","--03-10","--04-09","--03-05","2020-04-07","2020-10-27","2020-10-21","2020-06-13","--06-22"," 2020-07-23","2021-03-17"]
Clima=["Info no encontrada","Info no encontrada","Info no encontrada","Clouds, 11°, Humidity:58%","Clouds, 11°, Humidity:58%","Clouds, 11°, Humidity:58%","Info no encontrada","Info no encontrada","Clouds, 18°, Humidity:55%","Info no encontrada","Info no encontrada","Clouds, 27°, Humidity:83%","Info no encontrada","Clouds, 14°, Humidity:92%","Clouds, 23°, Humidity:83%","Clouds, 18°, Humidity:55%","Info no encontrada","Mist, 11°, Humidity:100%","Clouds, 11°, Humidity:58%" ]
eventos=0
for eventos in range(0,19):
    pagina["A"+str(eventos+2)] = Nombre[eventos]
    pagina["B"+str(eventos+2)] = Lugares[eventos]
    pagina["C"+str(eventos+2)] = Fecha[eventos]
    pagina["D"+str(eventos+2)] = Correo[eventos]
    pagina["E"+str(eventos+2)] = Telefono[eventos]
    pagina["F"+str(eventos+2)] = Facebook[eventos]
    pagina["G"+str(eventos+2)] = Twitter[eventos]
    pagina["H"+str(eventos+2)] = Instagram[eventos]
    pagina["I"+str(eventos+2)] = Clima[eventos]

libro.save(filename= "Excel.xlsx")
print("Se ha creado el archivo Excel")
time.sleep(2)
os.system("cls")

#Se guarda el contenido de la carpeta en un archivo .zip
#Se guarda en la misma ruta donde se encuentra la carpeta PIA IP
print("Se están guardandolos archivos en un .zip")
shutil.make_archive(rutaDesk + "/PIA IP", 'zip', rutaDesk + "/PIA IP")                                                              #contenido en el escritorio
print("Hecho!")
time.sleep(2)
os.system("cls")
