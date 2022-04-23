a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number  : "))
if a < b:
    if a < c :
        print(a,"is smallest")
    else:
        print(c,"is smallest")
else:
    if b<c:
        print(b,"is smallest")
    else:
        print(c,"is smallest")
