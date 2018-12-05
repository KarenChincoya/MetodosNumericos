#requiered libraries
import numpy
import matplotlib.pyplot as plt

#Initial parameters
alpha = 0.1  # Prey growing up rate 
beta = 0.02  # Predator successful rate 
gamma = 0.3  # Predator decrease rate
delta = 0.01 # Pretator hunting successful rate && feeding rate, cuanto alimenta cazar una presa
 
#Function euler (Para las iteraciones) 
def euler(u, f, dt):
    return u + dt * lotka_volterra_function(u)  # y1 = y0 + f(x0,y0) * (x1-x0) 

#Lotka-Volterra equations
def lotka_volterra_function(u):
    x = u[0]
    y = u[1]
    return numpy.array([x*(alpha - beta*y), -y*(gamma - delta*x)])

#Tiempo (coordenadas en x)
T = 200.0         # Limite
dt = 0.25         # Incremento en el tiempo (coordenadas x)
N = int(T/dt) + 1 # Número de intervalos + 1
x0 = 40.          # Número inicial de presas
y0 = 9.           # Número inicial de depredadores
t0 = 0.

#Arreglo para almacenar la solución
solution = numpy.empty((N, 2))
#Valor inicial
solution[0] = numpy.array([x0, y0])

# use a for loop to call the function rk2_step()
for n in range(N-1):
    solution[n+1] = euler(solution[n], lotka_volterra_function, dt)

time = numpy.linspace(0.0, T, N)
x_euler = solution[:,0]
y_euler = solution[:,1]

