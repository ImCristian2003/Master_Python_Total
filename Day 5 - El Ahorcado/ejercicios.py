lista_numeros = [1, 2, 15, 7, 2]

def reducir_lista(lista):
    
    num_mayor = lista[0]
    
    for elem in lista:
        
        if lista.count(lista[elem]) > 1:
            
            primer_aparicion = lista.index(lista[elem])
            
            for i in range(0, lista.count(lista[elem])):
                
                if i == primer_aparicion:
                    
                    continue
                
                else:
                    
                    lista.pop(i)
                    
        if lista[elem] > num_mayor:
            
            num_mayor = lista[elem]
            
    lista.pop(lista.index(num_mayor))
    
    return lista
    
def promedio(lista):
    
    suma = 0
    
    for index, item in enumerate(lista):
        
        suma += item
        
    return suma/len(lista)

print(reducir_lista(lista_numeros))
print(promedio(lista_numeros))