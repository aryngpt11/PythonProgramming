class Mobile:
    fp='Yes'    #class Variable
    def __init__(self):
        self.model='Iphone'    #Instance variable
    def sm(self):
        print("Model:",self.model)  #instance method

    @classmethod #class Method
    def is_fp(cls):
        print("finger Print:",cls.fp) #Accessing class varible
rl=Mobile()
rl.sm()
Mobile.is_fp()
print()
Mobile.fp='No'
Mobile.is_fp()