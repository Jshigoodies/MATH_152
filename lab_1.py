from sympy import *
from sympy.plotting import (plot, plot_parametric)

# 1a
x = 4.2
y = 3.14
expression_1 = (sqrt(x+y))/(sqrt(x**2-y**2)) + (2*x) - (x*(y**2))
print("{:.3f}".format(expression_1))

# 1b
expression_2 = sqrt(x**2 + y**2)
expression_3 = x + y
print("{:.2f}".format(expression_2))
print("{:.2f}".format(expression_3))
print("My answer does not equal to the previous expression")

# 2a
P = 200000
r = 0.04
t = symbols("t")
top = (r/12)*(1+(r/12))**(12*t)
bot = (1+(r/12))**(12*t) - 1
R_payment = (P) * (top)/(bot)
print("$" + str("{:.2f}".format(R_payment.subs(t,15))) + " for 30 years")

print("$" + str("{:.2f}".format(R_payment.subs(t,30))) + " for 15 years") # problem bere

# 2b
month_pay_1 = R_payment.subs(t, 30) # 30 years
print("$" + str(month_pay_1 * 360))
month_pay_2 = R_payment.subs(t, 15) # 15 years
print("$" + str(month_pay_2 * 180))

# 3a

# Part 1: Entering expression using the numbers
print("Part 1")
plug_7 = (1/15.0)*(3*7**4 + 7**2 - 2)*(sqrt(7**2 + 1.0))
plug_1 = (1/15.0)*(3*1**4 + 1**2 - 2)*(sqrt(1**2 + 1.0))
print(plug_7 - plug_1)

# Part 2: Defining a and b
print("\nPart 2")
a = symbols("a")
b = symbols("b")
expression_b = (1/15)*(3*b**4 + b**2 - 2)*(sqrt(b**2 + 1.0))
expression_a = (1/15)*(3*a**4 + a**2 - 2)*(sqrt(a**2 + 1.0))
print((expression_b) - (expression_a))
print("=")

# Part 3: using subs command
print("\nPart 3")
x = symbols("x")
y = symbols("y")
expression_x = (1/15)*(3*x**4 + x**2 - 2)*(sqrt(x**2 + 1.0))
expression_y = (1/15)*(3*y**4 + y**2 - 2)*(sqrt(y**2 + 1.0))
print((expression_x.subs(x, 7)) - (expression_y.subs(y, 1)))

# 3b
x = symbols("x")
f = (1/15.0)*(3*x**4 + x**2 - 2.0)*(sqrt(x**2 + 1.0))
f_of_x = diff(f)
print(f_of_x)

# 4a
x = symbols("x")
f1 = sin(2*x)
f2 = 2*sin(x)
p = plot(f1,f2, (x, 0, 2*pi), show=false)
p[1].line_color = 'r'
p.show()

# 4b
solved = solve(sin(2*x) - 2*sin(x), x)
print("when f(x) = 0, then x equals ")
print(solved)

# 4c
x = symbols("x")
f1 = sin(2*x) - 2*sin(x)
f_prime = diff(f1)
# print(f_prime) # -2*cos(x) + 2*cos(2*x)
solved = solve(f_prime, x)
print(solved)