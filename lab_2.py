from sympy import *
from sympy.plotting import (plot, plot_parametric)
import math

# 1a
x = symbols('x')
f = (x**2)*(sqrt(x+2))
F = integrate(f, x)
print("Indefinite integral is: " + str(F.simplify()) + " + C")

# 1b

x = symbols('x')
f = (1)/(1+sqrt(x))**4
F = integrate(f, (x, 0.0, 1.0))
G = integrate(f, (x, 0, 1))

print("Indefinite integral is: " + str(F.simplify()) + " + C")

# 2a
x = symbols('x')
f = sin(x)/(cos(x))**2
# print(f)
F = integrate(f, x)
print("Integral of f(x) is " + str(F))

# 2b
print("tan(x)*(1/cos(x)) == f(x)")

# 2c
F = integrate(f, (x, 0, pi/4))
print(F)

# 2d
x = symbols('x')
g = tan(x)*(1/cos(x))
G = integrate(g, (x, 0, pi/4))
print(G) # same answer as the above

# 3a
x = symbols('x')
f = exp(2-x**2)
g = x**4
p = plot((f, (x, -2, 2)), (g, (x, -2, 2)), show=false)

p[0].line_color = 'r' # red is the f(x) and blue is the g(x)
p.show()

# 3b
inter = solve((f-g)*1.0, x)
x1 = inter[0]
x2 = inter[1]
y1 = f.subs(x, inter[0])
y2 = g.subs(x, inter[1])
print("Points of intersection is " + "(" + str(x1) + ", " + str(y1) + ")" + " and " + "(" + str(x2) + ", " + str(y2) + ")")


# 3c
area = integrate((f-g), (x,x1,x2))
print("The area is: " + str(area.simplify()))

# 4a
x = symbols('x')
f = sin(2*x)
g = cos(x)

p = plot((f, (x, 0, pi/2)), (g, (x, 0, pi/2)), show=false)

p[0].line_color = 'r' # red is the f(x) and blue is the g(x)
p.show()

# 4b
A = integrate((g-f), (x, 0, pi/6))
A = A + integrate((f-g), (x, pi/6, pi/2))
print(A)