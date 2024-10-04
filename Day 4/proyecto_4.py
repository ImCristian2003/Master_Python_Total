# La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
# algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
# para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
# número y el programa puede responder cuatro cosas distintas:

# 1. Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
# un número que no está permitido.
# 2. Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
# decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
# 3. Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
# misma manera.
# 4. Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
# intentos le ha tomado.

# Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
# número. Y así hasta que gane o hasta que se agoten los ocho intentos.
 
from random import *

result = False
num_attemps = 0
user_number = 0

#get user name
name = input("Type your name: ")

#get random number between 1 - 100
random_number = randint(1, 101)

print(random_number)

for i in range(8):
    
    user_number = int(input("What number are you thinking of?: "))

    #validations
    if user_number not in range(0, 101):

        print("Your number is out of range!")

    elif user_number < random_number:

        print("Your number is less than the number I'm thinking of")

    elif user_number > random_number:

        print("Your number is grater than the number I'm thinking of")

    else:

        num_attemps = i + 1
        result = True
        break


print(f"{name}, you got it with {num_attemps} attemps" if result else "Game over")