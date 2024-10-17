# Creea un software que funcione como el turnero de una farmacia que te pregunta qué trámite vienes a realizar 
# y te asigna un número de turno según el área a la que deseas dirigirte. 
# En nuestro caso, vas a crear el tunero para una farmacia que tiene tres áreas de atención: 
# perfumería, farmacia, y cosméticos. 
# Tu programa le tiene que preguntar al cliente a cuál de las áreas desea dirigirse, y le va a dar un número de 
# turno según a qué área se dirija. Por ejemplo, si elige cosmética le va a dar el número C-54 
# (“C” de cosmética). Luego de eso, nos va a preguntar si queremos sacar otro turno.
# Y repetirá todo el proceso. 

# Algunas cosas a tener en cuenta: 
# Los diferentes clientes van a ir sacando turnos para diferentes áreas (perfumería, farmacia, 
# cosmética), en diferentes órdenes, por lo que el sistema debe llevar la cuenta de cuántos turnos 
# ha dado para cada una de esas áreas, y producir el siguiente número de cada área a medida 
# que se lo pida.
# Por otro lado, el mensaje donde le comunicamos el número de espera al cliente, debería tener 
# algo de texto adicional antes y después del número. Por ejemplo, “su turno es (-el número de 
# turno con el del comienzo-)”, y luego algo así como “aguarde y será atendido”.

#imports
from utilidades import generadores  
#from utilidades import generadores, decoradores #forma recomendada en caso de pocos módulos

#instances
cosmetic = generadores.cosmetic_turn()
pharmacy = generadores.pharmacy_turn()
perfumery = generadores.perfumery_turn()

#functions
def validation(selection):

    if selection == 1:

        print(next(cosmetic))
        return 1

    elif selection == 2:

        print(next(pharmacy))
        return 1

    elif selection == 3:

        print(next(perfumery))
        return 1

    else:

        return 0

def system():

    while True:

        sel = int(input("""A qué área deseas dirigirte (Digite otro número para salir)
                        1. Cosméticos
                        2. Farmacia
                        3. Perfumería """))
        
        if validation(sel) == 0:

            break

        else:

            True

system()