#Conteo de Números Pares e Impares:
#Descripción: Imagina que estás diseñando un contador para analizar una serie de números. 
#Este programa debe ser capaz de procesar varios números y contar cuántos de ellos son pares y cuántos son impares.
#El programa solicitará al usuario que ingrese una cantidad de números. 
#A medida que se vayan introduciendo, se debe llevar un registro de cuántos son pares y cuántos son impares. 
#Al final del proceso, se mostrará un resumen indicando cuántos números pares e impares fueron ingresados. 
#El programa deberá continuar contando mientras se sigan ingresando números.

#Declaración:
num=int();
contadorpar=int();
contadorimpar=int();
fin=int();
#Inicialización:
num= 0;
contadorpar= 0;
contadorimpar= 0;
fin=0;
#PROGRAMA:
print("Este es un programa que analizara cuales numeros son pares y cuales impares.");
while fin!=2:
    num= int(input("Por favor ingrese un numero entero: "));
    if num%2==0:
        contadorpar+=1
    else:
        contadorimpar+=1
    fin=int(input("Si desea finalizar el conteo escriba 2, si desea continuar escriba cualquier otro numero: "));
print("Se han contado: ", contadorpar, "numeros pares y ", contadorimpar, "numeros impares.");