# Ejercicios 4

## Entrega Jueves 4 de Diciembre

1.  Generar datos con “corrimiento al rojo” para los datos del Anillo en 2d. Para ello debemos crear mapa de velocidad: 
en una vecindad de L/10 de cada punto "pivote" en los datos, encontrar el punto más cercano y generar una velocidad 
para este punto pivote en la dirección del punto más cercano proporcional a su distancia (v=dist*0.1). 
Guardar el nuevo punto con coordenadas    <img src="https://latex.codecogs.com/gif.latex?\mathbf{r}=(x,&space;y&plus;v\cdot\hat{j})" title="\mathbf{r}=(x, y+v\cdot\hat{j})" />


2. Cambiar el código de la función de correlación con estimador de Landy-Salay, para que sea anisotrópico y guarde la componente 
de cada distancia en X y Y. 

   a) Con este código calcular la función de correlación anisotrópica del ejercicio anterior 
   y graficarla como gráfica de densidad en 2d (se puede usar imshow de matplotlib)
   
   b) (BONUS) Descomponer en la base de Legendre para encontrar encontrar el monopolo, cuadrupolo y hexadecapolo. 
   Graficarlos todos en un mismo plot. [ Para realizar este ejercicio debes cambiar la función de correlación a coordenadas polares ]
  
