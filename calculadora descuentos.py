#Calculadora de descuentos:
#Diseña un programa que calcule el precio final de un producto después de aplicar un descuento basado en el valor de la compra.

#Declaración.
precio=float();
descuento=float();
final=float();
#Inicialización.
precio=0;
descuento=0;
final=0;
#PROGRAMA:
precio=float(input("Ingrese el valor del producto seleccionado: "));
if precio<50:
    print("El producto no recibe ningun descuento.");
elif precio>=50 and precio<=100:
    final=precio*0.9;
    print("El producto tiene un 10% de descuento. El precio final es de: ", final);
else:
    final=precio*0.8;
    print("El producto tiene un 20% de descuento. El precio final es de: ", final);