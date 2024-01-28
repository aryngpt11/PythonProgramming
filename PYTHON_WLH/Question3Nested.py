n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))
n3=int(input("Enter the number2: "))

if(n1>n2):
    if(n1>n3):
        print(n1,"n1 is greater")
    else:
        print(n3, "n3 is greater")
else:
    if(n2>n3):
        print(n2,"n2 is greater")
    else:
        print(n3,"n3 is greater")