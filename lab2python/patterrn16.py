for i in range(5,0,-1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print('A',end="")
        else:
            print('B',end="")
    print()
