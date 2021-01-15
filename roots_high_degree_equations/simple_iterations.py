import numpy as np
import matplotlib.pyplot as plt

'''
Method: Simple Iterations (for-loop)
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Date: Jan. 14, 2021
'''

MAX_ITERATIONS = 101
DEGREE_OF_ACCURACY = 0.000001

def function(x):
    return (2 * x ** 2 + 3) / 5

convergence_function = lambda x: (2 * x ** 2 + 3) / 5
divergence_function = lambda x:  1/np.cos(x)

# Lists to save values for plotting
xlist = list()
xnewlist = list()
itrlist = list()

x = 0
for iteration in range(1, MAX_ITERATIONS):
    x_new = divergence_function(x)

    xlist.append(x)
    xnewlist.append(x_new)
    itrlist.append(iteration)

    if abs(x_new - x) < DEGREE_OF_ACCURACY:
        break
    x = x_new
print(f'The root : {x_new:.3f}')
print(f'The number of iterations : {iteration:2d}')


# plotting
plt.plot(itrlist, xlist, 'b-o', itrlist, xnewlist, 'r-*')
plt.legend(['x', 'xnew'], loc='lower right')
plt.xlabel('iterations')
plt.ylabel('x')
plt.grid()
plt.show()