#medir la eficiencia de los procesos
import time
import timeit#saber el tiempo de ejecución de un bloque de código

def prueba_for(numero):

    lista = []

    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):

    lista = []
    contador = 1

    while contador <= numero:
        lista.append(contador)
        contador +=1
    return lista

# inicio = time.time()#inicio del temporizador
# prueba_for(15)#ejecución
# final = time.time()#final del temporizador

# print(final - inicio)#imprimir la diferencia

# inicio = time.time()
# prueba_while(15)
# final = time.time()

# print(final - inicio)

#saber tiempo de ejecución de bloques de código
#ejecución/declaración
declaracion = '''
prueba_for(15)
'''

#código
mi_setup = '''
def prueba_for(numero):

    lista = []

    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number=100000)#number = número de veces que se ejecuta el código
print(duracion)