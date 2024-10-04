# El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente 
# una serie de guiones que representa la cantidad de letras que tiene la palabra. 
# El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la 
# palabra oculta, el sistema le va a mostrar en qué lugares se encuentra. 
# Pero si el jugador dice una letra que no se encuentra en la palabra oculta, 
# pierde una vida.

from random import choice

lista_palabras = ["elefante", "carretera", "bicicleta", "computadora", "television", "biblioteca", "mariposa", "hipopotamo", "refrigerador", "aventura"]

def play_ahorcado(palabra):

    print(palabra)

    for letra in palabra:

        print("_", end=" ")

def vidas():

    cont_vidas = 6

    while cont_vidas > 0:

        cont_vidas -= 1

play_ahorcado(choice(lista_palabras))