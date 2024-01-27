sp=int(input("Enter the sp value: "))
cp=int(input("Enter the cp value: "))

if(sp>cp):
    profit=sp-cp
    print("The shopkeeper gets profit of rs: ",profit)
else:
    loss=cp-sp
    print("The shopkeeper gets loss of rs: ",loss) 