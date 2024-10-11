class CD:

    def __init__(self, titulo, canciones):
        self.titulo = titulo
        self.canciones = canciones

    #Metodo para cambiar la forma en que se muestra la clase cuando se llama a 
    #la instancia directamente
    def __str__(self):
        return f"Album: {self.titulo}"
    
    #Cambiar el comportamiento cuando se pida el largo de la clase
    def __len__(self):
        return self.canciones
    
mi_cd = CD("Métricas Frías", 15)
print(mi_cd)#metodo __str__