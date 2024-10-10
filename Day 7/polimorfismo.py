#Polimorfismo -> 2 o más objetos son diferentes pero pueden ejecutar un mismo objeto
#al llamarse igual

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice muu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice beee")


vaca1 = Vaca('Lola')
oveja1 = Oveja('Nube')

#almacenar las instancias en un array
animales = [vaca1, oveja1]

#iterar las instancias
# for animal in animales:
#     animal.hablar()

def animal_habla(animal):
    animal.hablar()