#Resolución del sistema de manera gráfica con respecto al tiempo

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

plt.figure("Evolución temporal", figsize=(8,5))
plt.title("Evolución temporal")
plt.plot(t, solucion[:, 0], label='presa')
plt.plot(t, solucion[:, 1], label='depredador')
plt.xlabel('tiempo')
plt.ylabel('población')
plt.legend()
plt.show()