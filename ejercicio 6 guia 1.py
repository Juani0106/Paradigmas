nom=str();
cant=int();
nom="";
cant=0;
nom=input("ingrese un nombre de usuario: ");
cant=len(nom);
cant=cant%2
if cant==0:
	print("La cantidad de letras de su nombre de usuario es par")
else:
	print("La cantidad de letras de su nombre de usuario es impar")