#Descripción: Estás creando una herramienta que ayuda a los estudiantes a llevar un registro de sus calificaciones y obtener su promedio.
#El objetivo de la aplicación es permitir que el estudiante ingrese varias calificaciones una por una y luego calcule el promedio de todas ellas.
#El programa debe pedir al usuario que ingrese las calificaciones de manera secuencial. 
#Una vez que se hayan ingresado todas las notas, deberá calcular y mostrar el promedio al estudiante. 
#Asegúrate de que el programa permita ingresar varias calificaciones sin que se detenga antes de tiempo y que el promedio sea calculado correctamente cuando el usuario decida 
# finalizar.

#Declaración:
Nota= float();
suma_nota= float();
Fin=int();
Cantidad_notas=int();
#Inicialización:
Nota= 0;
suma_nota= 0;
Fin=0;
Cantidad_notas=1;
#PROGRAMA:
print("Este es un programa creado para poder calcular el promedio de tus calificaciones.\n");
Nota=float(input("Ingrese la calificación: "));
suma_nota+=Nota;
Fin=int(input("Si desea finalizar el calculo escriba 2, si desea continuar escriba cualquier otro numero: "));
while Fin!=2:
    Nota=float(input("\nIngrese la calificación: "));
    suma_nota+=Nota;
    Cantidad_notas+=1
    Fin=int(input("\nSi desea finalizar el calculo escriba 2, si desea continuar escriba cualquier otro numero: "));
print("\nLa calificación final es: ", suma_nota//Cantidad_notas);