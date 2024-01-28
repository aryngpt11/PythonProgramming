""" list=[10,20,30,40,50,60,70]
for i in list:
    print(i) """

""" i=2
while(i<101):
    print(i)
    i+=2 """


""" n=int(input("Enter the value: "))

for i in range(n):
    print("*****") """

n=int(input("Enter the value: "))
for i in range(n):
    for j in range(1,n+1):
        print(j,end=" ")
    print("")

