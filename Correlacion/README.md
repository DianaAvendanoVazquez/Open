# Ejercicios 2

## Entrega Jueves 19 de Noviembre


1. Crea una caja en 2d de tamaño 1000 con las siguientes distribuciones
 
    a) puntos en una malla cuadriculada de distancia (10x10 cada retícula)
  
    b) 1000 puntos sobre un disco de radio 300
  
    c) 1000 puntos sobre un anillo con radio mayor 300 y radio menor 290 
    
    d) 50 anillos con 100 untos cada uno cuyos centros están distribuidos aleatoriamente sobre la caja 

2. Haz un algoritmo que calcule la función de correlación con DD/RR-1 con el mismo número de puntos aleatorios que datos, y comprueba que si usas muestras aleatorias la función de correlación es cero. Cambia el número de puntos y el tamaño de *bin*, y observa qué ocurre.

3. Calcula la función de correlación para cada una de las cajas de datos del inciso anterior, usando los estimadores de

    a) Peebles-Hauser
  
    b) Davis-Peebles
  
    c) Hamilton
    
    d) Landy-Szalay

y recuerda escoger un bin adecuado para ver las señales. Utiliza 10 veces el número de puntos en las muestras aleatorias que con los datos.

4. Observar como cambia la función de correlación con el número de puntos aleatorios.
    a) Usando 1 archivo con 1, 5, 10 y 50 veces el número de puntos que los datos, y promedia los histogramas
    b) Usando 1 archivo con 1, 5, 10 y 50 veces el número de puntos que los datos, y promedia las funciones de correlación
    c) Usando 1, 5, 10 y 50 archivos de muestras aleatorias con el mismo número de puntos que los datos

5. Integra la función de correlación sobre la distancia para cada estimaor del inciso 3 y considerando sólo los datos del inciso 1a, y 1d.

6. Modifica el tamaño de la caja a 2000 y 3000, manteniendo la densidad constante de puntos con respecto al inciso 1), calcula 
de nuevo las funciones de correlación para cada estimador del inciso 2) y comparalas, considerando sólo los datos del inciso 1a, y 1d.

BONUS 1. ¿Puedes generar un código que tenga condiciones periódicas en la caja al calcular la función de correlación si la distancia máxima de interés es un décimo del tamaño de la caja? Hazlo sólo para los datos 1a y 1d.

BONUS 2. Trata de paralelizar tu código para usar mejor los procesadores de tu computadora

