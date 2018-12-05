#Numero de presas en funcion del número de depredadores

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#%matplotlib inline

#función que representa el sistema de ecuaciones de forma canónica
def df_dt(x, t, a, b, c, d):
    
    dx = a * x[0] - b * x[0] * x[1]
    dy = - c * x[1] + d * x[0] * x[1]
    
    return np.array([dx, dy])

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

solucion = odeint(df_dt, conds_iniciales, t, args=(a, b, c, d))

plt.figure("Presas vs depredadores", figsize=(8,5))
plt.title("Población de presas en función de los depredadores")
plt.plot(solucion[:, 0], solucion[:, 1])
plt.xlabel('presas')
plt.ylabel('depredadores')
plt.show()