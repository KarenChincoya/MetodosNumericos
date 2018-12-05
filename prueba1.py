#Resolución del sistema de manera gráfica con respecto al tiempo

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#%matplotlib inline

# Parámetros
a = 0.1
b = 0.02
c = 0.3
d = 0.01

# Condiciones iniciales
x0 = 40
y0 = 9
conds_iniciales = np.array([x0, y0])

# Condiciones para integración
tf = 200
N = 800
t = np.linspace(0, tf, N)

#función que representa el sistema de ecuaciones de forma canónica
def df_dt(x, t, a, b, c, d):
    
    dx = a * x[0] - b * x[0] * x[1]
    dy = - c * x[1] + d * x[0] * x[1]
    
    return np.array([dx, dy])

#x es el arreglo de valores iniciales
#t son los rangos, t0 son las cond iniciales
def euler(x, t, a, b, c, d, ti, tf, N):
    x0 = x[0]
    y0 = x[1]
    h = (tf-ti)/N
    algo = x
    for k in range (0,N-1):
        m = df_dt(x, t, a, b, c, d)
        y1 = y0 + h*m 
        t1 = x + h
        algo.concatenate(y1)
        print("t1 = "+t1)
        print("y1 = "+y1)
        t0 = t1
        y0 = y1
        
    return algo

#solucion = odeint(df_dt, conds_iniciales, t, args=(a, b, c, d))

def function(x, y):
    return -y + np.sin(x)

solucion = euler(conds_iniciales, t, a, b, c, d, 0, tf, N)

for x in range(0,10):
    print(solucion[x])

