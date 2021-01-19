'''
Method: Linear Regression
Course: Programming Numerical Methods in Python
Date: Jan. 18, 2021

Curve fitting is to find the equation of the curve that passes through the given data points with least deviation from
the points. Thus, the main difference between interpolation and curve fitting is that the latter does not have to
coincide all given data points.
'''


import numpy as np

from numpy import array, sum, mean
x = array([3, 4, 5, 6, 7, 8],float)
y = array([0, 7, 17, 26, 35, 45],float)
n = len(x)
sum_x = sum_x2 = sum_xy = sum_y = 0

for i in range(n):
    sum_x += x[i]
    sum_x2 += x[i]**2
    sum_xy += x[i]*y[i]
    sum_y += y[i]

x_mean = sum_x/n
y_mean = sum_y/n

a = (y_mean*sum_x2 - x_mean*sum_xy)/(sum_x2 - n*x_mean**2)
b = (sum_xy - x_mean*sum_y)/(sum_x2 - n*(x_mean**2))
print('The straight line equation')
print(f'y = {a:.3f} + {b:.3f}*x')


x = array([3, 4, 5, 6, 7, 8])
y = array([0, 7, 17, 26, 35, 45])
n = len(x);
x_mean = x.mean()
y_mean = y.mean()
a = (y_mean*sum(x**2) - x_mean*sum(x*y))/(sum(x**2) - n*x_mean**2)
b = (sum(x*y) - x_mean*sum(y))/(sum(x**2) - n*x_mean**2)
print('The straight line equation')
print(f'y = {a:.3f} + {b:.3f}*x')