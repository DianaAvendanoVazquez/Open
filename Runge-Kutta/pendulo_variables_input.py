
# coding: utf-8

# In[13]:



#---------------------------------------------------
#paqueterias
import math as math
import numpy as np
import matplotlib.pyplot as plt
import time

#declaración de constantes
beginning = time.perf_counter()#comienzo del contador de tiempo
#intento de runge-kutta 3r orden

l = float(input('Introduzca un valor para la longitud en metros:')) #longitud del péndulo en [m]
n = int(input('Introduzca el numero de iteraciones a calcular:')) #numero de iteraciones
tf=5*np.pi #tiempo final
t0 = 0 #tiempo inicial en segundos[s]
theta0= 1 #condición inicial de theta
v0 = 0
g = 9.81 #aceleración de la gravedad en [m/s2]
k = -g/l
dt =(tf-t0)/n #tamaño del diferencial de tiempo

constantes = time.perf_counter() #primer corte de timepo en las constantes

ContadorConstantes = constantes - beginning #cuenta cuanto tiempo tardó en calcular desde su inicio hasta el corte


#definimos las variables

t = np.arange(t0,tf+dt,dt) #tiempo en el que mediremos nuestro péndulo, de 0s a 180s
theta = np.zeros(len(t))
v = np.zeros(len(t))
theta[0] = theta0
v[0] = v0


    #---------------------------------------------------------------------------
                    #RungeKutta
    #---------------------------------------------------------------------------
for i in range(1,len(t)):
    
    dv=k*np.sin(theta[i-1])
#primer correccion
    j1=dt*dv
    dv = k*np.sin(theta[i-1] + dt/2) + j1/2
   # dv1=j1/2 + dv
#segunda correccion
    j2 = dt*(dv)
    dv = k*np.sin(theta[i-1] + dt/2) + j2/2
#    dv1 = j2/2 + dv
#tercera correccion
    j3= dt*dv 
    dv = j3 + k*np.sin(theta[i-1] + dt)
#cuarta correccion
    j4 = dt*(dv)
    
    v[i] = v[i-1] + (j1 + 2*j2 + 2*j3 + j4)/6
    theta[i] = theta[i-1] + dt*v[i-1]

    #---------------------------------------------------------------------------
    #solución exacta 
    #---------------------------------------------------------------------------
Theta = np.sin(((-k)**(1/2))*t) #ecuación de posición
#print('theta',np.sin(t))
dTheta = ((-k)**(1/2))*np.cos(((-k)**(1/2))*t) #ecuación de la velocidad
ddTheta = (-k)*np.sin(((-k)**(1/2))*t) #ecn. de aceleración


#--------------------------------------------------
       # Graficas
#---------------------------------------------------

fig, ax = plt.subplots()
plt.title('Posiciones para ángulos pequenos')
plt.grid()
ax.plot(t, Theta, '-c', label='solución exacta')
ax.plot(t, theta, '--r', label='solución usando RK')
plt.legend(bbox_to_anchor =(0.7, 1.3), ncol = 2) #posición de la caja de leyenda
plt.show()   

fig, ax = plt.subplots()
plt.title('velocidades angulares para ángulos pequenos')
plt.grid()
ax.plot(t, dTheta, '-c', label='solución exacta')
ax.plot(t, v, '--r', label='solución usando RK')
plt.legend(bbox_to_anchor =(0.7, 1.3), ncol = 2)  #posición de la caja de leyenda
plt.show()

