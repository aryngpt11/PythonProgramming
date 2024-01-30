
#find the sum of n njumbers

"""

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





def addAllNum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(addAllNum(2,3,4,5))

#**kwargs

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)
studentInfo(name="Aryan",roll_no=29,percentage=81)