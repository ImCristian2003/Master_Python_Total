# El programa va a elegir una palabra secreta y le va a mostrar al 
# jugador solamente una serie de guiones que representa la cantidad 
# de letras que tiene la palabra. El jugador en cada turno deberá elegir 
# una letra y si la letra se encuentra en la palabra oculta, el sistema 
# le va a mostrar en qué lugares se encuentra. 
# Pero si el jugador dice una letra que no se encuentra en la palabra 
# oculta, pierde una vida.

#import random
from random import choice

#array declaration
hidden_word = ["elefante", "carretera", "bicicleta", "computadora", "televisión", "biblioteca", "mariposa", "hipopótamo", "refrigerador", "aventura"]

#func to validate the word
def validate(array_validacion):

    for item in array_validacion:

        if item == "_":

            return True
        
        else:

            continue

    return False

#func to start que game
def play(palabra, letras, avance):

    print(palabra)
    checker = 0
    cont = 0

    for indice, letra in enumerate(palabra):

        if letra == letras:

            avance[indice] = letras
            cont += 1

        else:

            continue

    return avance, 0 if cont >= 1 else -1


#func to the total attemps
def attemps(palabra):

    check_array = []

    for letra in palabra:

        print("_", end=" ")
        check_array.append("_")

    total_attemps = 6

    print(f"Tienes un total de {total_attemps} intentos.")

    print(palabra)

    while total_attemps > 0:

        print(f"Tienes {total_attemps} vidas")
        letter = input("Ingresa una letra: ")
        check_array = play(palabra, letter, check_array)[0]

        if validate(check_array):

            print(check_array)
            total_attemps += (play(palabra, letter, check_array)[1])

        else:

            print(check_array)
            break

    return check_array

attemps(choice(hidden_word))