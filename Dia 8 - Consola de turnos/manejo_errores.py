def suma():
    n1 = int(input("número 1: "))
    n2 = int(input("número 2: "))

    print(n1 + n2)


try:
    #Código a probar
    suma()

except TypeError:
    #Código a ejecutar en caso de error
    print("Estás intentando concatenar tipos distintos")

except ValueError:
    #Código a ejecutar en caso de error
    print("Ingresaste algo diferente de un número")

else:
    #Código a ejecutar si no hay error
    print("Suma correcta")

# finally:
#     #Código que se ejecuta sea como sea
#     print("Eso fué todo")