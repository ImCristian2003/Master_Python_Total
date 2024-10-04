#importar librerías
from random import *

aleatorio = randint(1,5) #uniform trae un float aleatorio

print(aleatorio)

colores = ['azul', 'gris', 'purpura', 'naranja']
print(choice(colores))#Escoger aleatoriamente

#revolver una lista
numeros = list(range(5,51,5))

shuffle(numeros)

print(numeros)