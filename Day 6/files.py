import os
#print(os.getcwd())  # Imprime el directorio actual

#Traer el archivo a una variable
archivo = open('Day 6/prueba1.txt', 'a') #2° parametro indica el modo en que se abre
#r -> solo lectura
#w -> vaciar archivo y excribir (Si no existe crea uno nuevo)
#a -> escribir a partir del último punto

#Traer todos los datos del archivo
#leer = archivo.read()

#Traer el archivo en forma de lista
#todas = archivo.readlines()

#Escribir dentro del archivo
#archivo.write('Hola mundo!')

#escribir con varios strings
#archivo.writelines(['hola', 'cómo', 'estás'])

#Obtener ruta del directorio en trabajo
#ruta = os.getcwd()

#modificar la ruta del directorio actual
#ruta = os.chdir('')

#crear nuevo directorio/carpeta
#ruta = os.makedirs('')

archivo.close()