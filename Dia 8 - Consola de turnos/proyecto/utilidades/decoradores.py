#decorators

def decorate_turn(func):
    def wrapper(*args, **kwargs):
        # Creamos el generador llamando a la función original
        generator = func(*args, **kwargs)
        
        # Usamos un ciclo infinito para gestionar los valores del generador
        try:
            while True:
                print("Su turno es: ")
                value = next(generator)  # Obtiene el siguiente valor del generador
                yield value  # Devolvemos el valor generado
                #print("Aguarde su turno")
        except StopIteration:
            # Cuando el generador termine, el bucle se rompe
            return
    return wrapper


