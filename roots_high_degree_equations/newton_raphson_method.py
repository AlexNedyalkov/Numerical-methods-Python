"""
Method: Simple Iterations (for-loop)
Section: Newtown=Raphson method
Course: Programming Numerical Methods in Python
Date: Jan. 14, 2021

The Newton-Raphson method (also known as Newton's method) is a way to quickly find a good approximation for the root
of a real-valued function f(x)=0. It uses the idea that a continuous and differentiable function can be
approximated by a straight line tangent to it.
"""
function = lambda x: 2*x**2 - 5*x +3
derivative_function = lambda x: 4*x - 5
MAX_ITERATIONS = 101
DEGREE_OF_ACCURACY = 0.000001

x = 0
iterations = 0

for i in range(1, MAX_ITERATIONS):
    iterations += 1
    x_new = x - function(x) / derivative_function(x)
    if abs(x_new - x) <= DEGREE_OF_ACCURACY:
        break
    x = x_new

print(f'The root : {x_new:.3f}')
print(f'The number of iterations : {iterations:2d}')