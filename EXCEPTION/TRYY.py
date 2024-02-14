""" a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
try:
    c=a/b
    print("result",c)
except:
    print("cannot divide by zer0")
else:
    print("Aryan")
 """

""" class Mobile:
    def __init__(self,m):
        self.m=m
    def show(self):
        print("Model:",self.m)
rl=Mobile("Iphone")
rl1=Mobile("samsung")
rl.show()
rl.show()
rl1.show()
rl1.show() """

class MyClass:
    def show(self):
        print("I am a Method")
x=MyClass()
x.show()
