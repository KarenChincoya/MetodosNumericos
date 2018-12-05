import numpy as np
from matplotlib import pyplot as plt
#basic parameters

x0 = 0 
y0 = 1
xf = 10
n = 101

deltaX = (xf-x0)/(n-1)

#Create an array with the x values, number of parameters
x = np.linspace(x0, xf, n) 

#Generate the y values, 1st generate the array
y = np.zeros([n])

#define the funtion
def function(x, y):
    return -y + np.sin(x)

#euler's method implementation
#Set the inital value
y[0] = y0

for i in range(1, n):
    y[i] = y[i-1] + np.sin(x[i-1]) + function(x[i-1], y[i-1])

#print the results
for i in range(0, n):
    print(x[i], y[i])

#print the function
plt.plot(x,y, 'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Aproximación utilizando la función de Euler")
plt.show()
