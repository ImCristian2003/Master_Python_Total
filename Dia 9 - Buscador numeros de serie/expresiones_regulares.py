#expresiones regulares
import re

texto = "Si necesitas ayuda llama al 658-598-9977 para ayuda las 24 horas"

# patron = "ayuda"

# for hallazgo in re.finditer(patron, texto):
#     print(hallazgo.span())#span halla la ubicación inicial y final de la palabra

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')#r avisa que es una expresión regular y re.compile y () dividen en grupos

resultado = re.search(patron, texto)#buscar la expresión
#print(resultado.group(2))

clave = input("Clave: ")

patron = r'\D{1}\w{7}'

validacion = re.search(patron, "D434ddf3")

def verificar_email(email):
    
    patron = r'\w+@\w{1,10}.com'

    validacion = re.search(patron, email)

    return validacion

print(verificar_email("cc100156@gmail.com"))

#print(validacion)