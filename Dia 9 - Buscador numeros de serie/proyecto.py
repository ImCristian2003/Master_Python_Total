# Tu trabajo es crear un Buscador de Números de Serie. ¿Qué es eso? Es un programa que se encargue de buscar números de serie que cumplan un determinado formato, dentro de un arbol de carpetas.
# Tu programa va a recorrer todos los archivos y subcarpetas de un directorio raiz (en este caso, la carpeta que acabas de descomprimir), y va a buscar cualquier string que coincida con un patrón de número de serie. Sabemos que no puede haber más de un número de serie por archivo.
# Para lograrlo vas a usar el módulo os para abrir e iterear por el directorio, y las expresiones regulares para encontrar el formato de número de serie correcto.
# A los fines de este ejercicio, estas son las condiciones de formato que deben cumplir los hallazgos:
# - [N] + [tres carateres de texto] + [-] + [5 números]
# Por ejemplo: Nryu-12365
# La presentación en pantalla de los hallazgos debe ser un listado en formato de tabla, que respete el siguiente formato de ejemplo:
# ----------------------------------------------------
# Fecha de búsqueda: [fecha de hoy]

# ARCHIVO		NRO. SERIE
# -------		----------
# texto1.txt	Nter-15496
# texto25.txt	Ngba-85235

# Números encontrados: 2
# Duración de la búsqueda: 1 segundos
# ----------------------------------------------------

# IMPORTANTE
# * La 'Duración de búsqueda' debe estar redondeada hacia arriba
# * No olvides que la mejor forma de recorrer un arbol de carpetas, probablemente sea con el método walk() de os.
# * Observa que la fecha de búsqueda debe ser la fecha del día en que ejecutes el código, por lo que necesitas echar mano del módulo datetime.
# * Animate a encontrar una manera de mostrar la fecha de hoy con el formato dd/mm/aa.
# * Para informar la duración de la búsqueda al final de tu presentación, vas a necesitar del módulo time.
# * Recuerda que para poder imprimir todo en formato de tabla puedes usar los caracteres especiales \t para tabular.

#imports
import os
from pathlib import Path
from datetime import date, datetime
import re
import time
import timeit
import math

#change current directory
os.chdir(Path('C:/PUPy/Dia 9 - Buscador numeros de serie'))

#set rute
rute = Path('C:/PUPy/Dia 9 - Buscador numeros de serie')
directory_rute  = Path(rute/'Proyecto Dia 9'/'Mi_Gran_Directorio')

def printDirectoryAll():

    cont = 0

    #formated current date
    print(f"{date.today().strftime("%B %d of %Y")}\n")#format current date

    print("ARCHIVO\t\tNRO. SERIE")
    print("-------\t\t----------")
    #browse folder
    inicio = time.time()#temp start
    for carpeta, subcarpeta, archivo in os.walk(Path(rute/'Proyecto Dia 9'/'Mi_Gran_Directorio')):

        for arch in archivo:
            
            #error control
            try:
                #'with' helps to open and close at the same time the file to avoid errors and performance problems
                with open(Path(carpeta) / arch, 'r') as my_file:
                    content = my_file.read()

                #validation to print the file
                my_pattern = r'N\D{3}-\d{5}'
                validate = re.search(my_pattern, content)#validation

                if validate:
                    
                    print(f"{arch}\t{validate.group()}")
                    cont += 1

            except Exception as e:

                print("Error desconocido al querer abrir el archivo")

    final = time.time()#temp start

    print(f"\nNúmeros encontrados: {cont}")
    print(f"Duración de la búsqueda: {math.floor(final-inicio)} segundos")

        
printDirectoryAll()