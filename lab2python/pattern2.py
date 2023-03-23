#Python program to print reverse of a pattern

a=int(input("Enter the no: "))
for i in range(a,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
