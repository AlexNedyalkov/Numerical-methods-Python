'''
Method: Simpson's 3/8 Rule
Section: Numerical Integration
Course: Programming Numerical Methods in Python
Date: Feb 01, 2021
'''

'''
It is very similar to Simpson’s 1/3 rule except that three strips are taken into account and, consequently,
 four points will be included at each time. 
'''

from math import sin, pi
f = lambda x: x*sin(x)
a = 0
b = pi/2
n = 6
h = (b - a) / n
S = (f(a) + f(b))
for i in range(1, n, 3):
    S += 3*(f(a + i*h) + f(a + (i+1)*h))
for i in range(3, n, 3):
    S += 2*f(a + i*h)
Integral = 3*h/8 * S
print('Integral = {Integral}')