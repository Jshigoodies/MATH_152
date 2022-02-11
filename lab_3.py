from sympy import *
from sympy.plotting import (plot, plot_parametric)

# 1a
x = symbols('x')
y1 = sin(x)
y2 = cos(x)
intersection = solve(y1 - y2, x)
# print(intersection) # for the x coordinate
equation = (pi*cos(x)**2 - pi*sin(x)**2)
volume = integrate(equation, (x, 0, intersection))
print("= " + str(volume))

# 1b
x = symbols('x')
equation = 2 * pi * (pi/4 - x) * (cos(x) - sin(x))
volume = integrate(equation, (x, 0, intersection))
print(volume)

# 2a
x = symbols('x')
f = 4*sqrt(2*x + 2)
g = 2*x**2 + 4*x + 1

p = plot((f, (x, 0, pi/2)), (g, (x, -1, 2)), show=false)

p[0].line_color = 'r' # red is the f(x) and blue is the g(x)
p.show()

# 2b
inter = solve((f-g)*1.0, x)
print("x for the intersection is: " + str(inter))

# 2c
equation = pi*(10 - f)**2 - pi*(10 - (2*x**2 + 4*x + 2))**2
ans = integrate(equation*1.0, (x, 2, 5.657))
print("Volume = " + str(ans))

# 2d
a = integrate(2*pi*(2-x)*(4*sqrt(2*x+2) - (2*x**2+4*x+2)), (x, 0, 1))
print("Volume = " + str(a))

# 3a
y = symbols('y')
equation = pi*(4-y**2)
# print(equation)
equation_ = integrate(equation, y)
# print(volume_equation)
konstant = equation_.subs(y, -2) # the origin is in the middle of the sphere.
# print(konstant)
volume = 1000*((equation_) - (konstant))

ans = solve((volume) - 10000, y)
print("for 10000 liters")
print("height is: " + str(2 + ans[0].evalf()))

print()

ans = solve((volume) - 20000, y)
print("for 20000 liters")
print("height is: " + str(2 + ans[0].evalf()))

print()

ans = solve((volume) - 30000, y)
print("for 30000 liters")
print("height is: " + str(2 + ans[0].evalf()))

# 3b
x, y = symbols('x y')
p1 = plot_implicit(Eq(x**2 +y**2, 4),aspect_ratio=(1.0,1.0))

# 4a
y = symbols('y')
equation = volume * 9800 * (2-y)
work = integrate(equation, (y, -2, 2))
print(work)

# 4b
# 4b -------------- I have no idea where it went

work = integrate(equation, (y, -2, 1.44846001070777))
print("for 10000 L")
print(work.evalf())

print()

work = integrate(equation, (y, -2, 2.25967528339242))
print("for 20000 L")
print(work.evalf())

print()

work = integrate(equation, (y, -2, 3.19686524762472))
print("for 30000 L")
print(work.evalf())