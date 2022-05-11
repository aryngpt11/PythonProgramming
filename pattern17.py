for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,2*i):
        print('*',end="")
    print()
for i in range(4,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,2*i):
        print('*',end="")
    print()
