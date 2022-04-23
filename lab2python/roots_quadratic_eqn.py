#python program to find the roots of a quadratic equation

from math import sqrt
print("Quadratic function : (a * x**2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = b**2 - 4*a*c
if d > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(d))/(2*a))     
    x2 = (((-b) - sqrt(d))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif d == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")

