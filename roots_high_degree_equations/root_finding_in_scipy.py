from scipy.optimize import root, newton, bisect, fsolve

def quadratic_function(x): return 2*x**2 - 5*x + 3

print(newton(quadratic_function, 0))