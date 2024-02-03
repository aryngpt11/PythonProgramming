#using normal if else 
""" a=input("Enter the string: ")
c=a.lower()
print(c)
if c==c[::-1]:
    print("yes it is palindrome")
else:
    print("not a palindrome") """

#using recusion
def check_paindrome(str):
    clean_str=(str.replace(" ","")).lower()
    reverse_str=clean_str[::-1]
    return clean_str==reverse_str
str=input("enter a string")
if check_paindrome(str)==True:
    print("PAlindrome")
else:
    print("not palindrome")