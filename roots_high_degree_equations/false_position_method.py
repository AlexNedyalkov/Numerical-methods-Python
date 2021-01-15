'''
Method: False Position Method
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Date: Jan. 15, 2021

In false position method, the position of xh is the intersection point of the x-axis and the line connecting the two
falsepoints (x1, y1) and (x2, y2).
'''

from math import cos

def false_position_method(fn, x1, x2, tol = 0.001, ilimit = 100):
    y1 = fn(x1)
    y2 = fn(x2)
    xh = 0
    ipos = 0
    if y1 == 0:
        xh = x1
    elif y2 == 0:
        xh = x2
    elif y1 * y2 > 0:
        print('No root exists within the given interval.')
    else:
        for ipos in range(1,ilimit+1):
            xh = x2 - (x2-x1)/(y2-y1) * y2
            yh = fn(xh)
            if abs(yh) < tol:
                break
            elif y1 * yh < 0: # if y1 and yh have opposite signs
                x2 = xh
                y2 = yh
            else:
                x1 = xh
                y1 = yh
    return xh, ipos

def quadratic_function(x): return 2*x**2 - 5*x + 3       # Example 1
trig_function = lambda x: x**2 + cos(x)**2 - 4*x  # Example 2

x1 = float(input('Enter the value x1: '))
x2 = float(input('Enter the value x2: '))
x, n = false_position_method(fn = quadratic_function, x1 = x1, x2 = x2)
print(f'The root: {x:.2f}')
print(f'The number of computed false positions: {n}')