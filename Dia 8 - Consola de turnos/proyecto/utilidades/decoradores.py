#decorators

def decorate_turn(func):

    def wrapper(*args):
        print("Su turno es: ")
        resultado = func(*args)
        print("Aguarde su turno")

        return resultado
    
    return wrapper
