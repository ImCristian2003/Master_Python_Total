#hacer pruebas con unittest de cambia_texto.py
import unittest
import cambia_texto

#clase para hacer las pruebas
class ProbarCambiaTexto(unittest.TestCase):

    #la función debe comenzar por test
    def test_mayusculas(self):
    
        palabra = "buen día"#parámetro que se va utilizar para la prueba
        resultado = cambia_texto.todo_mayusculas(palabra)#resultado que arroja la función
        self.assertEqual(resultado, "BUEN DÍA")#assertEqual(resultado, resultado esperado)


# Si el archivo se ejecuta directamente (es decir, no es importado por otro archivo), 
# el valor de __name__ será '__main__'.
# Esta línea de código verifica si el archivo es el que se está ejecutando directamente.
if __name__ == '__main__':
    unittest.main()