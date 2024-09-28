#Categoría de Velocidad
#Descripción: Imagina que estás desarrollando un software para un club de corredores que desea clasificar el rendimiento de sus miembros 
#según la velocidad promedio de una carrera reciente. El objetivo es determinar en qué categoría de velocidad se encuentra un corredor y 
#proporcionar la clasificación adecuada.
#El programa pedirá al usuario que introduzca la distancia recorrida en kilómetros y el tiempo tomado en minutos.
#Con esta información, se calculará la velocidad promedio. Dependiendo de cuán alta o baja sea esta velocidad, el corredor puede ser clasificado
#como alguien que tiene un ritmo más lento, moderado o rápido.
#Deberás mostrar esta clasificación al usuario, dejando que las circunstancias de la velocidad determinen la categoría.
#Declaracion:
km=float();
t=float();
v=float();
#Inicializacion.
km=0;
t=0;
v=0;
#Programa:
km=float(input("Introduzca la cantidad de kilometros recorridos por el corredor: "));
t=float(input("Introduzca en minutos el tiempo que tardo el corredor en recorrer los kilometros: "));
v=km//t
print("La velocidad promedio del corredor es: ", v);
if v<=15:
    print("El corredor tiene un ritmo lento");
elif v<=30:
    print("El corredor tiene un ritmo moderado");
else:
    print("El corredor tiene un ritmo rapido");