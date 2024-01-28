#n=int(input("Enter size of list: "))
t=(10,20,30,40,50,60)
list=[]
for x in reversed(t):
    list.append(x)
output_t=tuple(list)
print(output_t)