""" l1=["a","b","c"]
l2=["d","e","f"]
#using Zip Function
dict1=dict(zip(l1,l2))
print(dict1.keys()) """

ipStirng=input("Enter String: ")
n=int(input("Enter n: "))

#cretaing dict for mirror operation
alphabets="abcdefghijklmnopqrstuvwxyz"
reverse_alphabets=alphabets[::-1]
dict1=dict(zip(alphabets,reverse_alphabets))

#finding the part of string where we want to mirror
prefix=ipStirng[0:n-1]
suffix=ipStirng[n-1:]

#findin the mirror string

mirror=""
for i in range(0,len(suffix)):
    mirror=mirror+dict1[suffix[i]]

#creating the final string
res=prefix+mirror
print(res)