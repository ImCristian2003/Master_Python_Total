# Ejercicio N°1
# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio

def evaluar_numero(array_n, posicion):

    array_n.sort()

    numero = array_n[posicion]

    return numero


def devolver_distintos(n1, n2, n3):

    suma = n1 + n2 + n3

    array = [n1, n2, n3]

    resultado = 0

    if suma > 15:

        resultado = evaluar_numero(array, 2)

    elif suma < 10:

        resultado = evaluar_numero(array, 0)

    else:

        resultado = evaluar_numero(array, 1)

    return resultado



#print(devolver_distintos(5, 4, 3))


# Ejercicio N°2
# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido", debería devolver ['d','e','i','n','o','r','t']

palabra = "entretenido"

def formatear_palabra(palabra):

    array = list(palabra)
    new_array = []

    for index, letra in enumerate(array):

        if array.count(letra) > 1:

            if index == array.index(letra):

                new_array.append(letra)

            else:

                continue

        else:

            new_array.append(letra)

    new_array.sort()

    return new_array

#print(formatear_palabra(palabra))


# Ejercicio N°3
# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def devolverTrue(n_evaluar,*args):

    if args.count(n_evaluar) > 1:

        return True
    
    else:

        return False
    
#print(devolverTrue(5,5,6,1,0,0,0,9,3,5))

# Ejercicio N°4
# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números 
# primos existentes en el rango que va desde cero hasta ese 
# número incluido, y va a devolver la cantidad de números 
# primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.

def esPrimo(num):

    cont = 0

    for i in range(1, num + 1):

        if num % i == 0:

            cont += 1

    validacion = False if cont > 2 else True

    return validacion

def contarPrimos(rango):

    cont = 0
    array = []

    for i in range(1, rango +1):

        if esPrimo(i):

            cont += 1
            array.append(i)

    return cont, array

print(contarPrimos(20))