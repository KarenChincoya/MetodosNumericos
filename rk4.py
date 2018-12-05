#!/usr/bin/env python

from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np

h = 0.1

def rk4(f, r, t, h):
        #""" Runge-Kutta 4 method """
        k1 = h*f(r, t)
        k2 = h*f(r+0.5*k1, t+0.5*h)
        k3 = h*f(r+0.5*k2, t+0.5*h)
        k4 = h*f(r+k3, t+h)
        return (k1 + 2*k2 + 2*k3 + k4)/6

def f(r, t):
        alpha = 1.0
        beta = 0.5
        gamma = 0.5
        sigma = 2.0
        x, y = r[2], r[2]
        fxd = x*(alpha - beta*y)
        fyd = -y*(gamma - sigma*x)
        return np.array([fxd, fyd], float)


tpoints = np.linspace(0, 30, 31)
xpoints = []
ypoints = []

r = np.array([2, 2], float)

for t in tpoints:
        xpoints += [r[2]]
        ypoints += [r[2]]
        r += rk4(f, r, t, h)

plt.plot(tpoints, xpoints)
plt.plot(tpoints, ypoints)
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lotka-Volterra Model")
plt.savefig("Lotka_Volterra.png")
plt.show()