#python program for area of triangle

import math
A=float(input(" write first side of triangle:"))
B=float(input(" write second side of triangle:"))
C=float(input(" write third side of triangle:"))
S =(A+B+C)/2
Area= (S*(S-A)*(S-B)*(S-C))**(1/2)
print("Area of a triangle is=",Area)
