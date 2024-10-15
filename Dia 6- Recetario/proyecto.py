# Tu código le va a dar primero la bienvenida al usuario, le va a informar
# la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
# cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
# estas opciones que tenemos aquí:
# 1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
# el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
# 2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
# escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
# a crear ese archivo en el lugar correcto.
# 3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
# una carpeta nueva con ese nombre.
# 4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
# a eliminar
# 5. La opción 5, le va a preguntar qué categoría quiere eliminar
# 6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código. 

#imports
import os
import shutil
from pathlib import Path
import numpy as np #arrays utilities

#save the user access route to recets
route = Path("C:/PUPy/Recetario Dia 6/Recetas")

#functions

#function to save all recets
def saveAll():

    recetas = []

    for recet in Path(route).glob("*/*"):

        recetas.append((recet.parents[0].name, recet.stem))

    return recetas

#function to show all recets
def showAll(recets):

    print("Estas son tus recetas disponibles: \n")

    for count, recet in enumerate(recets):

        print(f"{recets[count][0]} -> {recets[count][1]}")

#function to show only the categories
def showCategories(categ):

    array = []

    for count, cate in enumerate(categ):

        array.append(categ[count][0])

    return array

#function to show only the recets per category
def showRecets(rou, categ):

    array = []

    for index, recet in enumerate(Path(rou/categ).glob("*")):

        print(f"{index + 1}: {recet.stem}")
        array.append(recet)

    return array

#function to validate i
def validate(i):

    if i == 1: #read a recet

        elec = input(f"Elige una categoría ({', '.join(np.unique(showCategories(saveAll())))}):").capitalize()

        if len(elec) != 0:

            print(f"\nRecetas de {elec}:")
            recets = showRecets(route, elec)
            num_rec = int(input("\nDigita el número de la receta que quieres leer: "))

            archivo = open(Path(route/elec/recets[num_rec - 1]))
            
            print(archivo.read())

            archivo.close()

        else:

            print("Debes elegir una categoría")

    elif i == 2: #create a new recet with its content

        elec = input(f"Elige una categoría ({', '.join(np.unique(showCategories(saveAll())))}):").capitalize()

        if len(elec) != 0: 

            name = input("Escribe el nombre de la nueva receta: ")
            cont = input("Ahora el contenido: ")

            archivo = open(Path(route/elec/(name + '.txt')), 'w')
            archivo.write(cont)

            archivo.close()

            print("¡Nueva receta creada con éxito!")

        else:

            print("Debes elegir una categoría")

    elif i == 3: #create a new category

        elec = input("Digita el nombre de la nueva categoría: ")

        if len(elec) != 0:

            os.makedirs(Path(route/elec), exist_ok=True)

            print("Categoría creada con éxito o ya existente!")

        else:

            print("Debes digitar una categoría")

    elif i == 4: #read a recet

        elec = input(f"Elige una categoría ({', '.join(np.unique(showCategories(saveAll())))}):").capitalize()

        if len(elec) != 0:

            print(f"\nRecetas de {elec}:")
            recets = showRecets(route, elec)
            num_rec = int(input("\nDigita el número de la receta que quieres eliminar: "))

            ruta_archivo = Path(route/elec/recets[num_rec - 1])

            ruta_archivo.unlink()

        else:

            print("Debes elegir una categoría")

    elif i == 5: #delete a category

        elec = input(f"Digita el nombre de la categoría a eliminar ({', '.join(np.unique(showCategories(saveAll())))}): ")

        if len(elec) != 0:

            ruta_archivo = Path(route/elec)

            shutil.rmtree(ruta_archivo)

            print("¡Categoría eliminada con éxito!")

        else:

            print("Debes digitar una categoría")

    elif i == 6:

        print("Saliendo...")
    
    else:

        print("Elección incorrecta")


#function to choose the options
def chOptions():

    i = 0

    while i != 6:

        i = int(input("""
            Elige una de estas opciones:
            1 - Leer receta
            2 - Crear receta
            3 - Crear categoría
            4 - Eliminar receta
            5 - Eliminar categoría
            6 - Finalizar programa
        """))

        validate(i)

#execute functions
chOptions()

#validate(5)

#print(showRecets(route, "Carnes"))

#print(f"Las categorías disponibles son: {', '.join(np.unique(showCategories(saveAll())))}.")

#showAll(saveAll())

#print(showCategories(saveAll()))

#print(', '.join(np.unique(showCategories(saveAll()))))

#print(saveAll())