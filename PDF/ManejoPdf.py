import fitz
import re
import os
from openpyxl import Workbook
"""
Este script extrae el texto de un pdf y despues lo analisa con las expreciones
regulares para buscar la materia, maestro, hora y dia, esos datos los pasa a
un excel donde se guarda toda la informacion.
"""
materias = ("ALGEBRA LINEAL|PROGRAMA DE SEGURIDAD|"
            "PROGRAMACION PARA CIBERSEGURIDAD|"
            "LABORATORIO DE PROGRAMACION PARA |"
            "SEÑALES DE TRANSMISION|TEORIA DE AUTOMATAS")
dias = ("LU|MA|MI|JU|VI|SA|L-V|LU,MA y MI|LU y MI|"
        "MA y JU|MI y SA|MI y VI|JU y SA|MA,MI y JU|"
        "LU,MI y VI|LU y VI|MI y JU|MA y MI|MI,JU y VI|"
        "LU y JU|LU y MA|MA,MI y SA|LU,MI y JU|MA,MI y VI")
indice_re = 0
fila = 2
exprecion_Materia = re.compile(materias)
exprecion_Hora = re.compile(r'\d\d:\d\d-\d\d:\d\d')
exprecion_Maestro = re.compile(r'\w* \w* \w*( \w*)?')
exprecion_Dias = re.compile(dias)
lista_re = [exprecion_Materia,
            exprecion_Maestro,
            exprecion_Hora,
            exprecion_Dias]


# Se extrae el texto del pdf y se escribe en un txt
def extract_pdf(pdf):
    pdf_document = pdf
    document = fitz.open(pdf_document)
    number = document.pageCount
    for i in range(number):
        page = document.loadPage(i)
        text = page.getText("text")
        with open("proof.txt","a+") as file:
            file.write(text)

extract_pdf("C:/Users/Adrian/Documents/HORARIOS.pdf")
# Se crea el excel
libro = Workbook()
pagina = libro.active
datos = [("Materia","Maestro","Hora","Dias")]
columna = ["A","B","C","D"]

for i in datos:
    pagina.append(i)

with open("proof.txt","r") as file:
    for line in file:
        busca = lista_re[indice_re].search(line)
        if busca != None:
            pagina[columna[indice_re]+str(fila)] = busca.group()
            if indice_re == 3:
                indice_re = 0
                fila += 1
            else:
                indice_re +=1

libro.save(filename = "Materias.xlsx")
os.remove("C:/Users/Adrian/Desktop/Python/proof.txt")
print("Listo")
