# División con resto Plantear un algoritmo que permita informar, para dos valores a y b el resultado de la división
#  a/b y el resto de esa división.
#Declaracion
a=float();
b=float();
#Inicializacion
a=0;
b=0;
#programa
a=float(input("Ingrese el dividendo: "));
b=float(input("Ingrese el divisor: "));
print(f"El resultado de la division es: {a/b}");
print(f"El resto de la division es: {a%b}");