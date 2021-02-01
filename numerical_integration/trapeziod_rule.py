'''
Method: Trapezoidal Rule
Section: Numerical Integration
Course: Programming Numerical Methods in Python
Date: Feb. 1, 2021
'''

'''
The main idea of limited integration is to computed the area under a curve of a function between two limits, a and b,
 by means of analytical integration rules.
 
The numerical integration(the quadrature)is to compute the area under the curve of a given function by dividing
  the area into strips or regions that the area of each of them can be calculated by using simple mathematical rules
   then all areas are summed to get the total area under the curve from a to b

The accuracy of the numerical integration method highly depends on the number of divisions that cover the area under
 the curve precisely. The method is more efficient when it yields more accurate result with lesser divisions.
'''

from math import sin, pi
import numpy as np

f = lambda x: x*sin(x)
a = 0
b = pi/2
n = 500
h = (b-a)/n
# the sum of the values of the function at the end points divided by two
S = 0.5 * (f(a) + f(b))

# add all of the values at all other data points
for i in range(1, n):
    S += f(a + i*h)

integral = S * h
print(f'Integral: {integral}')

