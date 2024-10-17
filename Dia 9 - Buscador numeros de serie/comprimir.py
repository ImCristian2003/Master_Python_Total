#comprimir y descomprimir archivos
import zipfile
import os
import shutil
from pathlib import Path

#acción con zipfile
os.chdir(Path('C:/PUPy/Dia 9 - Buscador numeros de serie'))

#comprimir archivos dentro de un archivo
#mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')#archivo donde van a ir los archivos comprimidos

#mi_zip.write('mitexto.txt')#archivo que va a ser comprimido


#descomprimir archivo
#zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')#archivo que se va descomprimir

#zip_abierto.extractall()#extraer todos los archivos del archivo


#acción con shutil
#comprimir
#carpeta_origen = Path('C:/PUPy/Repaso')

#archivo_destino = 'Todo_comprimido'

#shutil.make_archive(archivo_destino, 'zip', carpeta_origen)#crear archivo comprimido
shutil.unpack_archive(Path('C:/Users/CADesarrollo02/Downloads/Proyecto+Dia+9.zip'), 'Proyecto Dia 9', 'zip')#descomprimir archivo