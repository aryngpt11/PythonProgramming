""" fruits=["apple","mango","Banana",10,20,30]
print(fruits)
print(type(fruits))
if "Banana" in fruits:
    print("yes present")
print(fruits[2]) """

list=[40,20,10,50,70]
#list.sort()
#list.sort(reverse=True)
#list.reverse()
#print(list)
newList=[]
for i in list:
    if(i>30):
        newList.append(i)
print(newList)