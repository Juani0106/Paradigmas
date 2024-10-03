#5. Conversión de medidas Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: 
# yardas pulgadas cenơmetros metros Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro =1000
a=float();
b=float();
sist=int();
a=0;
b=0
sist=0
a=float(input("Introduzca una medida en pies: "));
sist=int(input("""De los siguientes sitemas:
1-yardas
2-pulgadas
3-cm
4-metros
Elija a cual convertir la medida en pies: 
"""))
if sist==1:
	b=a*0.33
	print(f"La medida en yardas es: {b}");
elif sist==2:
	b= a*12
	print(f"La medida en pulgadas es: {b}");
elif sist==3:
	b=a*30.48
	print(f"la medida en centimetros es: {b}");
elif sist==4:
	b=a*0.3048
	print(f"la medida en metros es: {b}");
else:
	print("Error la opcion no es valida.")