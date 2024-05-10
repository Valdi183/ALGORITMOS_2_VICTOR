# VICTOR VALDIVIA CALATRAVA
## PARCIAL ALGORITMOS

### Ejercicio POO

### Ejercicio de recursividad:
En este ejercicio, se pide hallar el factorial de un número utilizando el metodo de recursividad.
La recursividad, trata de resolver un problema, dividiendo un solo problema en varios problemas más sencillos, de esta forma, tenemos una clase o metodo base, el cual es 
el metodo con el caso más sencillo, y una serie de clases o métodos recursivos que se llamen a ellos mismos hasta que el problema se reduzca en el de la clase base, y
sea resuelto por esta.

Hipotesis: Podemos calcular el factorial de un número utilizando recursividad.
Precondición: El número debe ser un entero no negativo.
Postcondición:  Obtendremos el factorial del número dado como salida.
Entrada: numero entero no negativo
Salida: El fatorial del numero dado

### Ejercicio Bubble Sort:
El metodo del bubble sort o de ordenacion de burbuja es un algoritmo simple de ordenamiento que recorre repetidamente una lista de elementos
y compara elementos adyacentes (los que estan al lado entre ellos). Si están en el orden incorrecto, los intercambia. Este proceso se repite hasta que 
no se requieran más intercambios, lo que indica que la lista está ordenada. Es un metodo muy utilizado para ordenar una lista añadiendo las condiciones 
que se quieran, por ejemplo: en orden creciente, en orden decreciente...

Ejemplo de uso para una lista de elementos enteros Ej: [34, 7, 23, 32, 5]
Hipotesis: Podemos ordenar una lista de elementos utilizando el método de ordenamiento de burbuja.
Precondicion: Tenemos una lista de elementos que deseamos ordenar en orden creciente
Postcondicion:  La lista estará ordenada en orden ascendente.
Entrada: Una lista de elementos a ordenar.
Salida: La misma lista ordenada en orden ascendente.
Proceso: Comenzamos desde el primer elemento de la lista (índice 0). Para los elementos siguientes, comparamos elemento a elemento, con el elemento
siguiente. si el elemento actual es mayor que el siguiente, se intercambian. Nos desplazamos al siguiente elemento y hacemos el mismo proceso.
Es importante recalcar, que cada vez que recorra la lista entera, se comprueben si los elementos estan en su sitio o no, para seguir aplicando el algoritmo.
Repetimos estos pasos hasta ordenar la lista.

### Ejercicio Functools