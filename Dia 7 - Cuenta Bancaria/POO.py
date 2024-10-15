#Cración de clases en py
class Pajaro:

    #definición de atributos de clase
    alas = True

    #definición de constructor
    def __init__(self, color):
        self.color = color

    #definición de metodos de instancia (acceden y modifican atributos del objeto)
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} mts")

    #definición de metodos de clase
    # - No pueden acceder a los atributos de instancia (constructor)
    # - Pueden modificar los atributos de clase
    # - Pueden usar los metodos de instancia
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")

    #definición de metodos estáticos
    # - Solo se llaman directamente desde la clase, no pueden modificar nada de la clase
    @staticmethod
    def mirar():
        print("Mirando")



#instancia del objeto
mi_pajaro = Pajaro("rojo")
mi_pajaro.volar(13)

#metodos que hacen referencia directa al objeto (metodos de clase)
Pajaro.poner_huevos(5) #metodo de clase
Pajaro.mirar() #metodo estático