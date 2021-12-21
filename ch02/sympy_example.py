
# ! Sympy example

from sympy import *

init_printing()
x = sympify("x")
f = x ** 2 * sin(x)
print(f)

# print(f * x)

# plot(f)

# exp1 = expand((x - 1) * (x + 1))
# print(exp1)

# exp2 = expand((x - 2) ** 3)
# print(exp2)

sol1 = solve(x**2 + 2*x -8)
print(sol1)

sol2 = solve(sin(x) - cos(x))
print(sol2)
