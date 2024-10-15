cont = 0
cont_pares = 0
cont_impares = 0
total_imp = 0
total_prom = 0
suma_total = 0
n = 1

while(n!=0):

    n = int(input(" Ingresa un número,(Digite 0 para terminar: "))
    
    if n == 0:

        break

    else:

        cont = cont + 1
        modulo = n % 2
        if(modulo == 0):
            cont_pares = cont_pares + 1
            
        else:
            cont_impares = cont_impares + 1
            total_imp += n
            totalprom = total_imp/cont_impares

        suma_total += n

print("Suma total: ", suma_total)
print("Total de numeros ingresados: ", cont)
print("Total de numeros pares: ", cont_pares)
print("Total de numeros impares:", cont_impares)
if(total_imp > 20):
    print("Suma alta: ", total_imp)
            
else:
    print("Suma baja: ", total_imp)

print("Suma total de impares: ",total_imp)
print("Promedio total: ",totalprom)