# Basic Classes Related - 
# Written by V I E R U S
# Classes/Object, Inheritance, Iterator, Scope
# Variables: var1-10
# Inheritance-------------------------------------------------
print("\n") #Empty Space
class MyClass3:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def Myfunc(self):
        print("My name is " + self.fname, self.lname)

# creating a child class
class MyChildclass(MyClass3):
    #keeps the inheritance of parents __init__
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        
    def subChildfunc(self):
        print("My name is " + self.fname, self.lname + "and idk if i could read")  
        
#puts in variables        
var4 = MyChildclass("Jared", "Smith")
#calls function in parent
var4.Myfunc()

print("\n") #Empty Space
#calls function in child
var4.subChildfunc()

