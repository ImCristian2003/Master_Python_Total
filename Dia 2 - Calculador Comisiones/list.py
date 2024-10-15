lista = ['a', 'c', 'b']
# print(lista[::-1])
lista[1] = 'i'#Las listas sí son mutables
lista.append('d')#Agregar elementos
#lista.pop(0)#eliminar elemento
print(lista)
lista.sort()#sort no devuelve nada (none)
print(lista)

for i in range(3):
    print(i+1)