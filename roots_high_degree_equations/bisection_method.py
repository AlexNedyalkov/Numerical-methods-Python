'''
Method: Bisectiom Method
Section: Roots of Higher-Degree Equations
Course: Programming Numerical Methods in Python
Date: Jan. 14, 2021
'''

function = lambda x: 2*x**2 -5*x +3

x1 = 0
x2 = 5
y1 = function(x1)
y2 = function(x2)

while (y1 < 0 and y2 > 0) or (y1 > 0 and y2 < 0):
    x_half = (x1 + x2)/2
