import bs4#navegar en el texto que genera requests
import requests
from pathlib import Path

#traer todo el contenido de la pagina web a una variable
resultado = requests.get('https://escueladirecta.com/courses')

#formatear todo el código para hacerlo más accesible
soup = bs4.BeautifulSoup(resultado.text, 'lxml')

#imprimir una etiqueta en forma de lista si son varias
#print(soup.select('title'))
#print(soup.select('title')[0].get_text())#obtener solo el texto sin la etiqueta

#para entrar a elementos dentro de otro elementos o seleccionar clases o id
#se usa como en css
#'.clase'
#'#id'
#'div span'#todos los span que hayan dentro de un id sin discriminación
#'div>span'#todos los span directos, que no tengan nada de por medio entre ellos
#y el div

# parrafo_especial = soup.select('h1')[0].get_text()
# print(parrafo_especial)

#extraer imágenes de un sitio web
imagenes = soup.select('img.course-box-image')

cont = 1

for i in imagenes:
    #traer el src del elemento
    print(i['src'])
    imagen = requests.get(i['src'])#almacenar el src de la imagen

    #cargar la imagen en un archivo nuevo en modo binario (wb)
    nombre_img = f"imagen{cont}.jpg"
    #ruta del directorio donde se va descargar la imagen
    url = Path('C:/PUPy/Dia 11 - Extractor Datos Web/img')

    #forma mejorada de abrir los archivos y cerrarlos
    with open(url/nombre_img, 'wb') as f:

        #pasar el código binario al archivo img para su interpretación
        f.write(imagen.content)

    cont += 1