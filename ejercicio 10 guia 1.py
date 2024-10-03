#10 Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.
PRECIO_DOLAR=1200
plata=float();
cambio=float();
plata=0
cambio=0;
cambio=float(input("""1-peso a dolar
2-dolar a peso
seleccione el tipo de cambio que quiere realizar:  """));
if cambio==1:
	plata=float(input("ingrese el monto a cambiar: "));
	print(f"La cantidad de dolares que recibira es de {plata/1200}");
if cambio==2:
	plata=float(input("ingrese el monto a cambiar: "));
	print(f"La cantidad de pesos que recibira es de {plata*1200}")