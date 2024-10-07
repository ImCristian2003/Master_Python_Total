import os

n = input("Nombre: ")
a = input("Apellido: ")

# Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')

# Output
print(f"Tu nombre completo es {n} {a}")