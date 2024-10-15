#Ciclo for
for i in range(5):
    print(i)

#Ciclo while
n = 5

#pas -> Salta un ciclo incompleto o no concretado
#break -> Sale del ciclo cuando se cumple una condición
#continue -> Omite todo el código restante y pasa a la iteracción directamente

while n < 7:
    print("Oelo")
    n += 1
else:
    "Llorela pa"

# numero = 51

# while numero >= 0:
    
#     numero -= 1
    
#     if numero % 5 != 0:
#         continue
    
#     print(numero)

#mi_lista = list(range(3,301,3))
#print(mi_lista)

#imprimir índice de una lista

# lista = ['a', 'b', 'c']

# for indice, item in enumerate(lista):

#     print(indice, item)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    
    if nombre[0] == "M":
        print(indice)

lista_numeros = [2,3,8,5,10]

for i in lista_numeros:

    print(i)