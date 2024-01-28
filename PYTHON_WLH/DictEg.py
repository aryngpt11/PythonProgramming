numbers={
    "john":8787878,
    "ria":34545,
    "joy":45755 
}
print(numbers)
""" print(type(numbers))
print(len(numbers)) """

#access items of dict
print(numbers["john"])
print(numbers.get("john"))
print(numbers.keys())

#updates values in dict

numbers["john"]=97955412
print(numbers)

#add two dict

num={
    "kia":234567
}
numbers.update(num)
print(numbers)

#printing values of a dict

""" for i in numbers:
    #print(i)
    print(numbers[i]) """

#for i in numbers.items():
for i,j in numbers.items():
   # print(i)
    print(i,j)


#nested dictonary

phones={
    "Area1":{
        "x":0,
        "y":1,
        "z":2
    },
    "Area2" :{
        "a":3,
        "b":4,
        "c":5
    }
}
print(phones["Area1"]["y"])
print(phones["Area2"]["c"])