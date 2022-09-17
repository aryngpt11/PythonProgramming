for i in range(5,0,-1):
    for j in range(1,i+1):
        print('*',end='')
    for j in range(1,10-2*i):
        print(' ',end='')
    for j in range (1,i+1):
        print('*',end='')
    print()
