#Python program to calculate the hypotenuse of a right angled triangle

import math
a = float(input(" enter value of a: "))
b = float(input(" enter value of b: "))
c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse is", c )
