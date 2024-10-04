text = "Texto de prueba"
# print(text[3])#Print word index
# print(text.replace("Texto", "Cadena"))#Reemplazar
# print(text.index("de"))#Busqueda de palabra
# print(text.rindex("e"))#Busqueda de palabra

print(text[2:])#De 2 hasta el final
print(text[::-1])#Invertir la cadena de texto
text_list = text.split()
#print(text_list[1])
#print(text.split("t"))#en split el parametro es el criterio de separación
print("-".join(text_list))
print(text.replace("e", "i"))
print("de" in text)