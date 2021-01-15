'''
Method: Bisectiom Method
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Date: Jan. 14, 2021
'''
DEGREE_OF_ACCURACY = 0.000001

function = lambda x: 2*x**2 -5*x +3

x1 = 1.2
x2 = 1.5
y1 = function(x1)
y2 = function(x2)

if y1*y2 > 0:
    print('No roots exist within given interval')
    exit
iterations = 0
while y1 * y2 <= 0:
    iterations += 1
    if y1 * y2 == 0:
        if y1 == 0:
            x_half = x1
        else:
            x_half = x2
        break
    x_half = (x1 + x2)/2
    y_half = function(x_half)
    if abs(y_half) <= DEGREE_OF_ACCURACY:
        break
    elif y1 * y_half < 0:
        x2 = x_half
    elif y2 * y_half < 0:
        x1 = x_half
    y1 = function(x1)
    y2 = function(x2)



print(f'The root: {x_half:.2f}')
print(f'Number of bisections: {iterations}')
