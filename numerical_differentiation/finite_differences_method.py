'''
Method: Forward Differences Approximation
Section: Numerical Differentiation
Course: Programming Numerical Methods in Python
Date: Aug. 19, 2021

The finite differences method is based on the idea of finding the slope of a line connecting two consecutive data points.

Theoretically, the finite differences approximation is derived from Taylor’s series expansion of f(x).
The expansion of f(xi+1)can be written as:

𝑓(𝑥𝑖+1)=𝑓(𝑥𝑖)+𝑓′(𝑥𝑖)ℎ+𝑓′′(𝑥𝑖)/2!*ℎ**2+𝑓′′′(𝑥𝑖)/3!*ℎ**3+⋯

By omitting the terms containing the second and higher derivatives, the difference formula becomes:
′(𝑥𝑖)= (𝑓(𝑥𝑖+1)−𝑓(𝑥𝑖))/ℎ+𝑂(ℎ)
The term O(h)indicates to the error resulting from the truncation made to obtain the difference.
'''


import matplotlib.pyplot as plt
import numpy as np

f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
h = 0.05
x = 0.1

dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
print('Solution by forward differences:')
print(f'f\'({x}) = {dff1:.2f}')
print(f'f\'\'({x}) = {dff2:.2f}')


# Central differences approximation
dfc1 = (f(x+h)-f(x-h))/(2*h)
dfc2 = (f(x+h)-2*f(x)+f(x-h))/h**2
print('\nSolution by central differences:')
print(f'f\'({x}) = {dfc1:.2f}')
print(f'f\'\'({x}) = {dfc2:.2f}')

# Backward differences approximation
dfb1 = (f(x)-f(x-h))/h
dfb2 = (f(x)-2*f(x-h)+f(x-2*h))/h**2
print('\nSolution by backward differences:')
print('f\'(%f) = %f'%(x,dfb1))
print('f\'\'(%f) = %f'%(x,dfb2))
print(f'f\'({x}) = {dfb1:.2f}')
print(f'f\'\'({x}) = {dfb2:.2f}')

# Central differences approximation
x = np.linspace(0,1,11)
dfc1 = (f(x+h) - f(x-h))/(2*h)
dfc2 = (f(x+h) - 2*f(x) + f(x-h)) / h**2

# Plotting results
plt.plot(x,f(x),'-k', x,dfc1,'--b', x,dfc2,'-.r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)','f \'(x)','f \'\'(x)'])
plt.grid()
plt.show()

