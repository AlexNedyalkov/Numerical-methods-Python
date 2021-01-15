import sympy

# declare variable as symbol
x = sympy.symbols('x')

# perform basic differentiation
print(sympy.diff(x**5))

# product rule f(x) = (x**2 + 1) * cos(x)
print(sympy.diff((x**2 + 1) * sympy.cos(x)))

# chain rule (x**2 + 1)**5
print(sympy.diff((x**2 + 1)**5))

# partial derivative

x, y = sympy.symbols('x y')

print(sympy.diff((x**2*y), x))
print(sympy.diff((x**2*y), y))