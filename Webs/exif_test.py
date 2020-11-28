# Enrique Adrian Gonzalez Martinez
# script que saca, modifica, elimina e imprime la metadata de las imagenes de un directorio
# profe le cambie el nombre porque al correr el script tenia conflictos con el modulo exif ya que tienen el mismo nombre
# ‎14‎/10/‎2020, ‏‎2:23 p. m.

import os
from exif import Image

ls = os.listdir('C:\\Users\\Adrian\\Pictures')
names = ['C:\\Users\\Adrian\\Pictures\\'+x for x in ls if x.endswith('.jpg') or x.endswith('.JPG')]

for name in names:
    with open(name,'rb+') as file:
        img = Image(file)
        print(name)
        try:
            opcs = [img.model, img.make, img.datetime, img.gps_latitude,
                    img.gps_latitude_ref, img.gps_longitude, img.gps_longitude_ref]
            for opc in opcs:
                print(opc)
        except:
            print('No se encontro metadata')

        print('Añadiendo model y mensaje')
        img.model = 'Redmi 7'
        img.mensaje = 'Enrique estuvo aqui'
        file.write(img.get_file())
        try:
            opcs = [img.model, img.make, img.mensaje, img.datetime,
                    img.gps_latitude, img.gps_latitude_ref, img.gps_longitude,
                    img.gps_longitude_ref]
            for opc in opcs:
                print(opc)
        except:
            print('No se encontro metadata')

        del img.model
        del img.mensaje
        print('Eliminando model y mensaje')
        try:
            opcs = [img.make, img.datetime, img.gps_latitude,
                    img.gps_latitude_ref, img.gps_longitude, img.gps_longitude_ref]
            for opc in opcs:
                print(opc)
        except:
            print('No se encontro metadata')