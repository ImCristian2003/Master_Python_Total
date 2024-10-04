#Print

# print("Oeloooo \"Mamabicho\"") #\ es un comodín para ingresar caracteres especiales
# print("Acá hay una línea \nY acá hay otra \n\tY otra con tab") #Saltos de línea y tabulación
# print('This isn\'t a number')

#input

# name = input("Type your name:")

# print(name)

#Concatenar cualquier tipo de dato en un string
cadena1 = "tu número es"
cadena2 = 5

print("Y ahora {} el {}".format(cadena1, cadena2))#con la función format
print(f"Y ahora {cadena1} el {cadena2}")#con f

#Ejercicio

nombre = input("Digita tu nombre: ")
total_ventas= int(input("Digita tus ventas totales: "))

comision = round(total_ventas * 0.13, 2)

print(f"{nombre}, tus ventas totales fueron de {total_ventas}.\nPor lo cual tu comisión es de {comision}")