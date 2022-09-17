#Python program to find roots of quadratic equatioh
import cmath
a=float(input("co-efficient of x**2__:"))
b=float(input("co-efficient of x__:"))
c=float(input("constant term of equation:"))
X=(-b+(cmath.sqrt(b**2-4*a*c)))/2*a
Y=(-b-(cmath.sqrt(b**2-4*a*c)))/2*a
print("roots of the equation is= ",X ,Y)
