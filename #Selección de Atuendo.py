#Selección de Atuendo
#Estás diseñando una aplicación que ayuda a las personas a elegir su atuendo diario basado en la temperatura y la posibilidad de lluvia.
#La aplicación debe hacer recomendaciones sobre qué tipo de ropa y accesorios son apropiados para el día.
#La aplicación pedirá al usuario que introduzca la temperatura en grados Celsius y si espera lluvia o no.
#Basado en la información ingresada, deberás decidir si el atuendo debe incluir algo más abrigado o más ligero, y si es necesario agregar algún
#accesorio adicional para protegerse del clima. Al final, deberás mostrar la recomendación completa al usuario, considerando tanto la temperatura
#como la posibilidad de lluvia.
#Declaracion:
temp=float();
clima=int();
#Inicialización:
temp=0;
clima=0;
#Programa.
print("Este es un programa para recomendar atuendos en base al clima y las probabilidades de lluvia que hay.");
temp=float(input("Ingrese la temperatura que hace en la ciudad: "));
clima=int(input("Ingrese 1 si hay probabilidades de lluvia, de lo contrario ingrese 2: "));
if temp<=20:
    if clima==1:
        print("Recomendamos que se ponga una campera y ademas que por precacución se lleve un paraguas.");
    else:
        print("Recomendamos que se ponga una campera.");
if temp>20:
    if clima==1:
        print("El dia va a estar lindo en cuanto a temperatura, pero si llega a llover le recomendariamos que salga con un paraguas y una camperita liviana.");
    else:
        print("El dia va a estar lindo, pero si quiere puede llevarse una camperita fina por si hay viento.");
