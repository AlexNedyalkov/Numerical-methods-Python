'''
Method: Secant
Section: Roots of High-Degree Equations
Course: Programming Numerical Methods in Python
Date: Jan. 15, 2021
'''

from math import cos

def secant(fn, x1, x2, tol=0.000001, maxiter=100):
    for iteration in range(maxiter):
        x_new = x2 - (x2 - x1) / (fn(x2) - fn(x1)) * fn(x2)
        if abs(x_new - x2) < tol:
            break
        else:
            x1 = x2
            x2 = x_new
    else:
        print("Warning: Maximum number of iterations is reached!")
    return x_new, iteration


quadratic_function = lambda x: 2 * x ** 2 - 5 * x + 3
trig_quadratic_func = lambda x: x**2 + cos(x)**2 - 4*x

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))

r, n = secant(quadratic_function, x1, x2, 0.00001, 1000)

print(f"Root = {r:.2f} at {n} iterations")

