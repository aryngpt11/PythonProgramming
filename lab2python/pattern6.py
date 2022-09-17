for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
