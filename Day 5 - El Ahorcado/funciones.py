from random import shuffle

def saludar(nombre):
    #imprimir resultado
    return f"Oelo {nombre}"

t = saludar("Cristian")

print(t)

############################Lista inicial##############################

palitos = ['|', '||', '|||', '||||']

#Mezclar items
def mezclar(lista):

    shuffle(lista)
    return lista

#Pedir intento
def probarSuerte():
    intento = 0

    while intento not in range(1,5):

        intento = int(input("Elige un número del 1 al 4: "))

    return int(intento)

#Comprobar intento
def checkIntento(lista, intento):

    if lista[intento - 1] == '|':
        print("A lavar trastes pa")
    else:
        print("De pura suerte se salvó")

lista1 = mezclar(palitos)
print(lista1)

suerte = probarSuerte()

resultado = checkIntento(lista1, suerte)

#print(abs(-67))