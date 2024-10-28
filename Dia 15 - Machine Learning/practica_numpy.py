import numpy as np#librería para ciencia de datos
import pandas as pd

#----------------------------------NUMPY-----------------------------------------
#array unidimensional
array_unidim = np.array([1, 2, 3, 4])

#array bidimensional
array_bidim = np.array([[1, 2, 3],
                        [4, 5, 6]])

#array tridimensional
array_tridim = np.array([[[1, 2, 3],
                        [4, 5, 6]],
                        [[7, 8, 9],
                         [10, 11, 12]]])


#atributos del array unidimensional (forma, n dimensiones, tipo datos, tamaño y tipo)
#print(array_unidim.shape, array_unidim.ndim, array_unidim.dtype, array_unidim.size, type(array_unidim))

#atributos del array bidimensional (forma, n dimensiones, tipo datos, tamaño y tipo)
#print(array_bidim.shape, array_bidim.ndim, array_bidim.dtype, array_bidim.size, type(array_bidim))

#atributos del array tridimensional (forma, n dimensiones, tipo datos, tamaño y tipo)
#print(array_tridim.shape, array_tridim.ndim, array_tridim.dtype, array_tridim.size, type(array_tridim))



#----------------------------------PANDAS-----------------------------------------
#pandas trabaja de la mano de numpy
datos = pd.DataFrame(array_bidim)#cuadro de datos estructurado a partir del array
#print(datos)

#array de tamaño 4x3, formado solo por unos (1)
unos = np.ones((4, 3))#dimensiones

# Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)
cero = np.zeros((2, 4, 3))

# Creamos un array de números en el rango de 0 a 100, con un paso de 5
array_1 = np.arange(0, 101, 5)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)
array_2 = np.random.randint(0, 10, (2, 5))

# Creamos un array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3 de alto, 5 de ancho)
array_3 = np.random.random((3, 5))

# Establecemos la "semilla" de números aleatorios en 27
np.random.seed(27)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5)
array_4 = np.random.randint(0, 10, (3, 5))


# Encontramos los valores únicos del array_4
np.unique(array_4)

# Extraemos el elemento de índice 1 del array_4
array_4[1]

# Extraemos las primeras dos filas del array_4
array_4[:2]

# Extraemos los dos primeros datos de las primeras dos filas del array_4
array_4[:2, :2]

# Creamos dos arrays de tamaño 3x4: uno relleno de números aleatorios entre 0 y 10, y otro relleno de unos
array_5 = np.random.randint(0, 10, (3, 4))
array_6 = np.ones((3, 4))

# invocamos el array_5
array_5

# invocamos el array_6
array_6

# Sumamos los dos arrays
array_5 + array_6

# Creamos ahora un array de tamaño (4,3) lleno de unos
array_7 = np.ones((4, 3))

# Intentaremos sumar los arrays 6 y 7
array_6 + array_7#solo se pueden hacer operaciones con arrays de las mismas dimensiones


# Entonces crearemos otro array de tamaño (4,3) lleno de unos
array_8 = np.ones((4, 3))

# Restamos el array_8 al array_7
array_6 - array_7

# Creamos otros dos arrays de tamaño 3x3 con números aleatorios del 1 al 5
array_9 = np.random.randint(1, 5, (3, 3))
array_10 = np.random.randint(1, 5, (3, 3))

# invocamos el array_9
array_9

# invocamos el array_10
array_10

# Multiplicamos los últimos dos arrays entre sí
array_9 * array_10

# Elevamos el array_9 al cuadrado
array_9**2

# Buscamos la raíz cuadrada del array_10
np.sqrt(array_10)

# Hallamos el promedio de los valores del array_9
array_9.mean()

# Hallamos el valor máximo de los valores del array_9
array_9.max()

# Hallamos el valor mínimo de los valores del array_9
array_9.min()

# Cambiamos la forma del array_9 por una de 9x1, y lo almacenamos como array_11
array_11 = array_9.reshape((9, 1))

# invocamos el array_11
array_11

# Transponemos el array_11
array_11.T

# Comparamos el array_9 y el array_10, para saber cuáles elementos del array_9 son mayores a los del array_10
array_12 = array_9 > array_10



# Veamos sus nuevos tipos de datos
array_12.dtype

# Alguno de los elementos del array_9 es igual su equivalente del array_10?
array_9 == array_10

# Comparamos nuevamente ambos arrays, en esta ocasión con >=
array_9 >= array_10

# Buscamos los elementos del array_9 que son mayores a 2
array_9 > 2

# Ordenamos de menor a mayor los elementos dentro del array_9
np.sort(array_9)









