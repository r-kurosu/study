from cmath import sin
import math
from re import U
import numpy as np
import matplotlib.pyplot as plt
import math


nx = 101
dx = 1 / (nx-1)
nt = 100
dt = 0.01 
c = -1  

x = np.linspace(0,1,nx)


u = [[0 for i in range(101)] for j in range(101)] 
for j in range(100):
    u[0][j] = np.sin(math.pi * j/100)


for k in range(100): 
    for j in range(1, 100):
        u[k+1][j] = 1/2 * u[k][j+1] + u[k][j] - 1/2 * u[k][j-1]

print(u[100])