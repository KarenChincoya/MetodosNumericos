#requiered libraries
import numpy 
import matplotlib.pyplot as plt

#Initial parameters
alpha = 0.1  # Prey growing up rate 
beta = 0.02  # Predator successful rate 
gamma = 0.3  # Predator decrease rate
delta = 0.01 # Pretator hunting successful rate && feeding rate, cuanto alimenta cazar una presa
 
#Function euler (Para las iteraciones) 
def nextValue(u, dt, k1, k2):
    suma1 = numpy.add(k1/2,k2/2)
    result = u + dt *(suma1)  # y1 = y0 + f(x0,y0) * (x1-x0) 
    print(result)
    return result

#Lotka-Volterra equations
def lotka_volterra_function(u):
    x = u[0]
    y = u[1]
    return numpy.array([x*(alpha - beta*y), -y*(gamma - delta*x)])

def lotka_volterra_function2(u, k1, h):
    x = u[0]+h
    y = u[1]+k1*h
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
    k1 = lotka_volterra_function(solution[n])
    xk1 = solution[n][0]+dt
    print("xk1 = ",xk1)
    yk1 = solution[n][1]+((k1[0]**2+k1[1]**2))*dt
    print("yk1 = ",yk1)
    k2 = lotka_volterra_function(numpy.array([xk1,yk1]))
    solution[n+1] = nextValue(solution[n], dt, k1, k2)

time = numpy.linspace(0.0, T, N)
x_euler = solution[:,0]
y_euler = solution[:,1]

x_max = numpy.max(solution[:,0]) * 1.05
y_max = numpy.max(solution[:,1]) * 1.05

x = numpy.linspace(0, x_max, 25)
y = numpy.linspace(0, y_max, 25)

xx, yy = numpy.meshgrid(x, y)
uu, vv = lotka_volterra_function(numpy.array([xx, yy]))
norm = numpy.sqrt(uu**2 + vv**2) #longitud del vectorcito
uu = uu / norm
vv = vv / norm

plt.figure("Campo de direcciones", figsize=(8,5))
plt.quiver(xx, yy, uu, vv, norm, cmap=plt.cm.gray) #para dibujar arrows, razon de cambio y norma
plt.plot(solution[:, 0], solution[:, 1])#solution[:, 0], solution[:, 1]
plt.xlim(0, x_max)
plt.ylim(0, y_max)
plt.title("Runge-Kutta orden 2: Campo de direcciones de la población de presas en función de los depredadores")
plt.xlabel('presas')
plt.ylabel('depredadores')
plt.show()