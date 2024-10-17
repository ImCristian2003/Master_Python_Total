import os
from pathlib import Path
import shutil
import send2trash

ruta = os.chdir(Path('C:/PUPy/Dia 9 - Buscador numeros de serie'))#cambiar ruta del directorio
#print(os.getcwd())#obtener ruta actual

# archivo = open('archivo.txt', 'w')
# archivo.write("Prueba")
# archivo.close()

#mover archivo a una ruta específica
#shutil.move('archivo.txt', 'C:\\PUPy\\Repaso')


#enviar archivos a la papelera
#ejecutar en el cmd la instalación (pip install send2trash)
#send2trash.send2trash('archivo.txt')#enviar archivo a la papelera de reciclaje (recomendado)

#print(os.walk(Path('C:/PUPy/Mi_Paquete')))

#imprimir las carpetas, son sus subcarpetas y archivos correspondientes
for carpeta, subcarpeta, archivo in os.walk(Path('C:/PUPy/Mi_Paquete')):

    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")

    for sub in subcarpeta:
        print(f'\t{sub}')

    print("los archivos son:")

    for arc in archivo:
        print(f'\t{arc}')
    print("\n")