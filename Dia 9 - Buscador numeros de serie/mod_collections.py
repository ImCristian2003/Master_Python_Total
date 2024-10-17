#colecciones
from collections import Counter, defaultdict, namedtuple

#counter ayuda a contar los elementos según se requiera (Counter)
numeros = [8,6,5,7,5,2,4,5,2,5,7,4,3,4,6]
print(Counter(numeros))

frase = "Al pan pan y al vino vino"
print(Counter(frase.split(' ')))

#diccionario por defecto (defaultdict)

mi_dic = {'uno':'verde', 'dos':'rojo', 'tres':'azul'}

#ayuda a que en caso de no existir una llave en un diccionario y se trate de
#imprimir, este la cree y le asigne 'nada'
mi_dic2 = defaultdict(lambda: 'nada')
print(mi_dic2['uno'])

#tupla nombrada (namedtuple)
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
noe = Persona('Noe', 1.75, 65)

print(noe[1])