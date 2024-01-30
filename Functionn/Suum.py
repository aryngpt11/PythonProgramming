def sumOneToN(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
n=int(input("Enter n: "))
output=sumOneToN(n)
print(output)

#nested function

def outer_function():
    x=1
    def inner_function():
        y=2
        result=x+y
        return result
    return inner_function()
output1= outer_function()
print(output1)