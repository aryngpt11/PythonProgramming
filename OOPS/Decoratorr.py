def decor(fun):
    def inner():
        print("if beforw enhancing function")
        fun()
        print("if after enhancing function")
    return inner


def num():
    print("we will use this function")
    print("and will enhance this in decorator")
num()
result=decor(num)
result()