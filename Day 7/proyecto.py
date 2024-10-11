# Crear una clase persona con los atributos:
#     - nombre y apellido
# Crear una clase cliente que herede persona con:
#     - atributos: numero_cuenta y balance
#     - métodos: uno para imprimir la clase con toda la información (método especial),
#     uno para depositar y otro para retirar
# Crear un código que permita elegir depositar, retirar o salir de manera reiterada


#imports
#import locale

# Establecer el locale para que use separadores de miles europeos
#locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

#main class
class Persona:

    #constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#hereditary class
class Cliente(Persona):

    #constructor
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.__numero_cuenta = numero_cuenta
        self.__balance = balance

    #methods
    def depositar(self, cantidad):
        
        #validate
        if cantidad > 0:
            self.__balance += cantidad

    #specials methods
    def __str__(self):
        return f"El usuario {self.nombre} {self.apellido} con cuenta {self.__numero_cuenta} tiene un balance de {self.__balance:,.2f}"


mi_cliente = Cliente("Cristian", "Cardona", "013548363", 10000000)
print(mi_cliente)