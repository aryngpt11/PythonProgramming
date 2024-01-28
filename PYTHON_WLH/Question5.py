n=int(input("Enter size of list: "))
list=[]
for i in range(n):
    num=int(input())
    list.append(num)
idx1=int(input("Enter value of idx1: "))
idx2=int(input("Enter value of idx2: "))
print(list)
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp
print(list)