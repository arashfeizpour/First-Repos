# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 01:57:48 2016

@author: Arash

point : lissajous figures

equation : x = sin(A * wx*t + phiX) , y = sin(B * wy*t + phiY)

method = Numerical : ---
 
"""

#imports
import numpy as np
import matplotlib.pyplot as plt

#variables
phiX = np.pi / 1
PhiY = np.pi / 2
wx = 1
wy = 1
A = 4 ; B = 5
x = 'np.sin(A * wx * t + phiX)'
y = 'np.sin(B * wy * t + PhiY)'
tt = [0]
xx = []
yy = []
dt = 0.1

#functions 
def calculator():
    global x ; global y
    while tt[-1] < 100 :
        t = tt[-1]
        x_new = eval(x)
        xx.append(x_new)
        y_new = eval(y)
        yy.append(y_new)
        t_new = tt[-1] + dt
        tt.append(t_new)

#body 
calculator()


#results and plots
fig = plt.figure()
plt.plot(xx,yy,'black')
plt.xlabel('x')
plt.ylabel('y')

##GuideLines
plt.plot([0,0],[-1,1],'k')
plt.plot([-1,1],[0,0],'k')

plt.show()





