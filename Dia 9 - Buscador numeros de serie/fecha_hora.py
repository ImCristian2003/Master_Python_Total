from datetime import datetime, date

#asignar una hora por defecto
#mi_hora = datetime.time(18, 56)

# #asignar fecha
mi_dia = datetime(2024, 6, 25)

nacimiento = date(1995, 3, 5)
defuncion = date(2086, 6, 19)

vida = defuncion - nacimiento
print(vida)