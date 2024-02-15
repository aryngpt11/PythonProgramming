""" def decor(fun):
    def inner():
        print("if beforw enhancing function")
        fun()
        print("if after enhancing function")
    return inner

@decor
def num():
    print("we will use this function")
    print("and will enhance this in decorator")
num() """
""" result=decor(num)
result() """
def decor1(num):
    def inner():
        b=num()
        multi=b*5
        return multi
    return inner
def decor(num):
    def inner():
        a=num()
        add=a+5
        return add
    return inner
#@decor
def num():
    return 10
num=decor(decor1(num))
print(num())