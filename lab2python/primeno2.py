#python program to print all prime numbers in a given interval

lower = int(input("enter lower value:"))
upper = int(input("enter upper value:"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
