# Basic Functions of Python - May 19, 2022
# Written by V I E R U S
# Function: created a function, used arguments/parameters, *args, default parameter value, Pass a list/For loop, return value
# Variables: myFunction0-5

#Functions----------------------------------------------------------
#Created a function, Consider this function 0
def myFunction():
    print("This is a Function")

myFunction()
print("\n") #Empty Space


#Argument
def myFunction1(fname):
    print(fname + " This is a Function")

myFunction1("Vie")
myFunction1("Alex")
print("\n") #Empty Space

#*args - when you don't know how many arguments will be passed through
def myFunction2(*fname):
    print(fname[2] + " This is a Function")

myFunction2("Vie", "Alex", "Sam", "Jo")
print("\n") #Empty Space


#Default Parameter Value
def myFunction3(fname = "Jo"):
    print(fname + ", This is a Function")

myFunction3("Vie")
myFunction3()
myFunction3("Alex")
print("\n") #Empty Space

 
#Passing a List
def myFunction4(fname):
    for x in fname:
        print(x)

firstNames = ["Vie", "Alex", "Sam", "Jo"]
myFunction4(firstNames)
print("\n") #Empty Space


#Return Value
def myFunction5(x):
    return x*5

print(myFunction5(3))
print(myFunction5(6))
print(myFunction5(9))
print("\n") #Empty Space


print("\nEND OF FUNCTIONS LESSON\n\n") #End of Function Lesson