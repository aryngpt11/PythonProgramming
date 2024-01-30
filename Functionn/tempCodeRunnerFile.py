def factorial(n):
    fact=0
    if n==0:
        fact= 1
    else:
        for i in range(1,n+1):
            fact*=i
    return fact



n=int(input("Enter the value of n: "))
ouput=factorial(n)
print("the factorial of",n,"is: ",ouput)