""" class ABC:
    def __init__(self):
        self.public_attribute=None
    def public_function():
        pass
boj1=ABC()  """

class Mobile:
    def __init__(self):
        self.m="IPhone" #instance variable
    def Show_model(self): #instance method
        print(self.m) #Accessing instance variable 
rm=Mobile()
rm.Show_model()

