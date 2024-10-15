# Escribe un programa que haga lo siguiente:

# Solicita al usuario que ingrese números, uno a uno, usando un ciclo while.

# - Calcula e imprime el promedio de los números.
# - Identifica cuántos de esos números son pares e impares, imprimiendo ambos 
# valores.
# - Suma todos los números impares y calcula el promedio entre esos numeros.
# - Si el número resultante de la suma de impares es mayor a 20, 
# imprime "Suma alta", de lo contrario imprime "Suma baja".

prom_num = 0
num_impares = 0
num_pares = 0
sum_impares = 0
sum_total = 0
cont = 0
init = 1

while init != 0:

    init = int(input("Digita un número (Digita '0' para terminar): "))

    if init == 0:

        break

    else:

        if init % 2 == 0:

            num_pares += 1

        else:

            num_impares += 1
            sum_impares += init

        sum_total += init
        cont += 1

print(f"El promedio de los números es: {sum_total/cont}")
print(f"Números pares: {num_pares}")
print(f"Números impares: {num_impares}")
print(f"La suma de los impares es: {sum_impares} y su promedio es {sum_impares/num_impares}")

if sum_impares > 20:

    print("Suma alta")

else:

    print("Suma baja")


