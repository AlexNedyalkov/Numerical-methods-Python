'''
Method: Simpson's 1/3 Rule
Section: Numerical Integration
Course: Programming Numerical Methods in Python
Date: Feb. 01, 2021
'''

'''
Simpson’s rules use weighing factors to calculate the integrals to improve the accuracy with lesser number of divisions.
 Unlike the trapezoidal rule which considers two points, xiand xi+1, to calculate a trapezoid’s area,
  Simpson’s rules use more than two points, i.e. multiple strips, in each turn. The values of f(x)at the multiple points
   are adjusted by weighing factors to minimize the error.
   
Simpson’s 1/3 rule:This method calculates the area of two strips at a time, thus, three values of x are taken into
 account at each turn. To cover the whole domain exactly, the number of strips, n, should even
'''


from math import sin, pi
f = lambda x: x*sin(x)
a = 0
b = pi/2
n = 6
h = (b - a) / n
S = f(a)+f(b)
for i in range(1, n):
    if i % 2 == 1:
        S += 4 * f(a+i*h)
    else:
        S += 2 * f(a + i*h)

integral = S*h/3
print('Integral value: ', integral)


