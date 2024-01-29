
#find the sum of n njumbers

""" n=int(input("Enter n: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum) 

n1=int(input("Enter n1: ")) """

""" def printHello():
    print("Aryan")
printHello()
 """
def add(n1,n2):
    sum=n1+n2
    return sum
x=50
y=35
print(add(x,y))

#positional argyment
print(add(55,25))

#keyword argument(named argument)

print("the sum is ",add(n1=3,n2=7))

#default arguments