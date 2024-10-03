medida=float();
tipo=int();
medida=0
tipo=0

tipo=float(input("""1- pies
2- pulgadas
elija el tipo de medida que desea usar: """))
if tipo==1:
	medida=float(input("ingrese la medida en pies a convertir: "));
	print(f"la medida ingresada en centimetros seria de: {medida*30.48}");
elif tipo==2: 
	medida=float(input("ingrese la medida en pulgadas a convertir: "));
	print(f"la medida ingresada en centimetros seria de: {medida*2.54}");