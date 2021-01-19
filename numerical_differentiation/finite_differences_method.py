'''
Method: Forward Differences Approximation
Section: Numerical Differentiation
Course: Programming Numerical Methods in Python
Date: Aug. 19, 2021
'''


f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
h = 0.05
x = 0.1

dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
print('Solution by forward differences:')
print(f'f\'({x}) = {dff1:.2f}')
print(f'f\'\'({x}) = {dff2:.2f}')