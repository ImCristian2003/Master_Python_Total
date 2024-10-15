# Proyecto para el día 2 del master en python
# vas a crear un programa que primero le pida al usuario que 
# ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un 
# poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres 
# letras a su elección y a partir de ese momento nuestro código va a procesar esa información 
# para hacer cinco tipos de análisis y devolverle al usuario la siguiente información: 
# 1. Primero: ¿cuántas veces aparece cada una de las letras que eligió?
# 2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto
# 3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última
# 4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
# 5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto 

text = input("Please enter a text to analize: ").lower()
letters = input("Now, type 3 letters or your choice (They must be separated by a space): ").lower()

letters_list = letters.split(" ")#Convert string to list

# 1 -> Repetitions of the entered letters
print(f"The letter \"{letters_list[0]}\" is repeated {text.count(letters_list[0])} times.")
print(f"The letter \"{letters_list[1]}\" is repeated {text.count(letters_list[1])} times.")
print(f"The letter \"{letters_list[2]}\" is repeated {text.count(letters_list[2])} times.\n")

# 2 -> How many letter are entered in the text
print(f"There are {len(text.split(" "))} words in the text.\n")

# 3 -> First and last word of the text
print(f"The first word is \"{text.split(" ")[0].capitalize()}\".")
print(f"The last word is \"{text.split(" ")[-1]}\".\n")

# 4 -> Text reverse
print(text[::-1] + "\n")
#print(text.split(" ").reverse())

# 5 -> Is python in the text?
print(text.find("python"))