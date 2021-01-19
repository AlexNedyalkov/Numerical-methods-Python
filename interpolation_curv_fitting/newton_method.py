'''
Method: Newton Interpolation
Section: Interpolation and Curve Fitting
Course: Programming Numerical Methods in Python
Date: Jan. 18, 2021
'''

import numpy as np

x = [0.0, 1.5, 2.8, 4.4, 6.1, 8.0]
y = [0.0, 0.9, 2.5, 6.6, 7.7, 8.0]
n = len(x) - 1
x_approximate = float(input("Enter the x for which to approximate: "))
differences_y = np.zeros(shape=(n + 1, n + 1))
differences_y[:,0] = y

y_product = differences_y[0, 0]

for j in range(n):
    for i in range(j+1, n+1):
        differences_y[i, j+1] = (differences_y[i,j] - differences_y[j, j])/(x[i] - x[j])

for i in range(n):
    x_prod = 1
    for j in range(i+1):
        x_prod *= x_approximate - x[j]
    y_product += x_prod * differences_y[i+1, i+1]

print(f'For x = {x_approximate  :.1f}, y = {y_product:.1f}')
