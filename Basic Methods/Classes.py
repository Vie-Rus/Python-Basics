# Basic Classes Related - 
# Written by V I E R U S
# Classes/Object, Inheritance, Iterator, Scope
# Variables: var2, var3
# Classes/Object----------------------------------------------
# Create a class 
class MyClass:
    classVar1 = 10        

#create an object
var1 = MyClass()
print(var1.classVar1)
print("\n") #Empty Space

#__init__() Function
class MyClass1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
var2 = MyClass1("Jared", 19)
print(var2.name , var2.age)
print("\n") #Empty Space
 
#Object Methods
class MyClass2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Myfunc(self):
        print("My name is " + self.name + " and idk how to read")
      
var3 = MyClass2("Jared", 19)
var3.Myfunc()
print("\n") #Empty Space

#Modify Object properties
var3.age = 21

#delete object
#del var3