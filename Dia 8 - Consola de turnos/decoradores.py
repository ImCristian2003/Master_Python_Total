#los decoradores modifican la funcionalidad de otras funciones

#ejemplo
def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula
    

#operacion = cambiar_letras('may')
#operacion('palabra')

#ejemplo decorador con saludo y despedida
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')

    return otra_funcion

@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())


mayuscula('palabra')

