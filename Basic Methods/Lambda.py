# Basic Lambda of Python - May 19, 2022
# Written by V I E R U S
# Lambda: Creating a lambda, add multiple values, double/triple/etc your value
# Variables: var1-3, doubleIt

#Lambda--------------------------------------------------------
#many args but one expression
#Creating a Lambda


x = lambda var1 : var1 +10
print(x(5))
print("\n") #Empty Space

#multiple values
x = lambda var1, var2, var3 : var1*var2*var3
print(x(5,10,15))
print("\n") #Empty Space

#NOTE: say an argument will be multipled with an unknown number, you would use lambda to help with that
def myFunc(a):
    return lambda var1 : var1*a

doubleIt = myFunc(2) #the 2 double its, add a 3 and it triples it, etc
print(doubleIt(4)) #the 4 is the var1
print("\n") #Empty Space

#doubles via word
def myFunc1(a):
    return lambda var1 : var1*a

doubleIt = myFunc1(2) #the 2 double its, add a 3 and it triples it, etc
print(doubleIt("Doubles it ")) #the 4 is the var1

print("\n") #Empty Space
print("\nEND OF LAMBDA LESSON\n\n") #End of Lambda Lesson