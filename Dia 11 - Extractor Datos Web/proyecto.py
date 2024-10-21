# crear un código que sea capaz de navegar en la página
# https://books.toscrape.com/ y extraiga todos los libros de la sección
# libros que tengan más de 3 estrellas, esto teniendo en cuenta que dicha
# sección cuenta con 1000 resultados por lo cuál están divididos en varias
# páginas

import bs4#navegar en el texto que genera requests
import requests
from pathlib import Path

#tener la base de la url
#los {} ayudan a formatear el string para asignarle un valor dinámico
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#lista de títulos con 4 o más estrellas
titulos_rating = []

#iterar páginas
for pagina in range(1, 21):

    #traer el contenido de cada página
    url_pagina = url_base.format(pagina)
    #traer todo el contenido de la pagina
    resultado = requests.get(url_pagina)
    #formatear todo el código
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar libros
    for libro in libros:

        #validar que tengan 4 o más estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0: 
        
            #guardar título en variable
            titulo_libro = libro.select('a')[1]['title']

            #agregar el libro a la lista
            titulos_rating.append(titulo_libro)


#ver los libros de 4 o más estrellas
for t in titulos_rating:
    print(t)