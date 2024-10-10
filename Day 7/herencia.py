#Anotaciones
# - Cuando hay una herencia multiple con un metodo en común, tiene en cuenta el metodo
#   de la clase que hereda primero la clase heredadora

#Clase padre
class Animal:

    def __init__(self, color):
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

#Clase hija
class Pajaro(Animal):

    def __init__(self, color, altura_vuelo):
        super().__init__(color)#añadir los atributos de instancia heredados en el constructor
        self.altura_vuelo = altura_vuelo

#Instancias
piolin = Pajaro("azul", 17)
piolin.nacer()