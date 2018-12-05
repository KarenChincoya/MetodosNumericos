#requiered libraries
import numpy 
import matplotlib.pyplot as plt

#Initial parameters
alpha = 0.1  # Prey growing up rate 
beta = 0.02  # Predator successful rate 
gamma = 0.3  # Predator decrease rate
delta = 0.01 # Pretator hunting successful rate && feeding rate, cuanto alimenta cazar una presa
 
#Function euler (Para las iteraciones) 
def nextValue(u, dt, k1, k2,k3, k4):
    suma1 = numpy.add(k1/6,2*k2, 2*k3+k4)
    result = u + dt *(suma1)  # y1 = y0 + f(x0,y0) * (x1-x0) 
    print(result)
    return result

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
    k1  = lotka_volterra_function(solution[n])
    k1e = ((k1[0]**2+k1[1]**2))

    xk2 = solution[n][0]+dt/2 
    yk2 = solution[n][1]+ k1e *dt/2
    k2  = lotka_volterra_function(numpy.array([xk2,yk2]))
    k2e = ((k2[0]**2+k2[1]**2))

    xk3 = solution[n][0]+dt/2
    yk3 = solution[n][1] + k2e*dt/2
    k3  = lotka_volterra_function(numpy.array([xk3,yk3])) 
    k3e = ((k3[0]**2+k3[1]**2))

    xk4 = solution[n][0]+dt
    yk4 = solution[n][1] + k3e*dt
    k4  = lotka_volterra_function(numpy.array([xk4, yk4]))

    solution[n+1] = nextValue(solution[n], dt, k1, k2, k3, k4)

time = numpy.linspace(0.0, T, N)
x_euler = solution[:,0]
y_euler = solution[:,1]


