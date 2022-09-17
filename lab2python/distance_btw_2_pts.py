#python program to compute the distance between the points (x1, y1) and (x2,y2)

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
d = ( (x2-x1)**2 + (y2-y1)**2 ) ** 0.5
print('Distance = %f' %(d))
