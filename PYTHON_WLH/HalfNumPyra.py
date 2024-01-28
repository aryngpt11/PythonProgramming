""" n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("") """


rows=int(input("Enter the number: "))
ascii_v=65
for i in range(rows):
    for j in range(i+1):
        alpha=chr(ascii_v)
        print(alpha,end=" ")
    ascii_v +=1
    print("")