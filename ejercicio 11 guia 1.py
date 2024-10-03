#Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.
sueldo=float();
sueldo=0;
sueldo = float(input("Ingrese su sueldo: "))
for i in range(1, 13):
    sueldo *= 1.10 
    print(f"Su sueldo en el mes {i} es de {sueldo} pesos");