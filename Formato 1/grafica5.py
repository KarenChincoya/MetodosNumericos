#equilibrio, cuando se alcanza la condicion de equilibrio

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

def C(x, y, a, b, c, d):
    return a * np.log(y) - b * y + c * np.log(x) - d * x

#más condiciones iniales
x_max = np.max(solucion[:,0]) * 1.05
y_max = np.max(solucion[:,1]) * 1.05

x = np.linspace(0, x_max, 100)
y = np.linspace(0, y_max, 100)
xx, yy = np.meshgrid(x, y)
constant = C(xx, yy, a, b, c, d)

plt.figure('distintas_soluciones', figsize=(8,5))
plt.contour(xx, yy, constant, 50, cmap=plt.cm.Blues)
plt.xlabel('presas')
plt.ylabel('depredadores')
plt.title("Puntos criticos con distintas condiciones iniciales (0,0) y ((γ/δ,α/β) )")

plt.show()

