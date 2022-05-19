# Basic Classes Related - 
# Written by V I E R U S
# Classes/Object, Inheritance, Iterator, Scope
# Variables: var1-10

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

print("\n") #Empty Space


# Iterator----------------------------------------------------
print("\n") #Empty Space
#String Iterator
var5 = "Dog"
varIter = iter(var5)
print(next(varIter)) # D
print(next(varIter)) # o
print("\n") #Empty Space


#Loop through an iterator, through String
for x in var5:
    print(x) # D o g
print("\n") #Empty Space


#Tuple Iterator
var6 = ("Dog", "Fish", "Cat")
varIter1 = iter(var6)

print(next(varIter1)) #Dog
print(next(varIter1)) #Fish
print("\n") #Empty Space


#Loop through an iterator, through tuple
for x in var6:
    print(x) # Dog Fish Cat
print("\n") #Empty Space


   
#Create a Class/Object Iterator
class MyInfo:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 5:
            z = self.a
            self.a += 1
            return z
        else:
            raise StopIteration
    
var7 = MyInfo()
varIter2 = iter(var7)

#Counts to 5
for x in varIter2:
    print(x)
print("\n") #Empty Space

print("\n") #Empty Space
# Scope-------------------------------------------------------
# variable only available from inside the region

#local Scope
def scopeFunc():
    var8 = 300
    print(var8)

scopeFunc()
print("\n") #Empty Space


#Function inside Function
def scopeFunc1():
    var9 = 200
    def innerScopeFunc():
        print(var9)
    innerScopeFunc()
scopeFunc1()
print("\n") #Empty Space


#Global Scope - variable outside function used by anyone > Python Basic Function
#Global Keyword - makes variable global

def scopeFunc2():
    global var10
    var10 = 100
    
scopeFunc2()
print(var10) # 100 Prints here
print("\n") #Empty Space 

print("\nEND OF CLASSES LESSONS\n\n") #End of Classes Lesson