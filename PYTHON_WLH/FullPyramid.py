n=int(input("Enter the no of rows: "))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(k,end=" ")
    print("")