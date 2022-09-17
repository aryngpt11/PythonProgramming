for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    for j in range(1,10-2*i):
        print(' ',end='')
    if i==5:
        k=i-1
    else:
        k=i
    for j in range(1,k+1):
        print(k-j+1,end='')
    print()
