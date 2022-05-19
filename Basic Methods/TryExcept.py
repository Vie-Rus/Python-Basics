# Basic Try/Except of Python - May 19, 2022
# Written by V I E R U S
# Try/Except: Created a try/except, NameError, Else Loop, Final, Raise Exception, TypeError

#Try/Except------------------------------------------------------------------------------------
#Created a try/except
try:
    print(x)
except:
    print("Error since x is not defined")
print("\n") #Empty Space


#NameError
try:
    print(x)
except NameError:
    print("Variable x not defined")
except:
    print("Error, something else is wrong")
print("\n") #Empty Space


#Else
try:
    print("Hello ")
except NameError:
    print("Error, something wrong")
else:
    print("Nothing went wrong this time")
print("\n") #Empty Space


#Finally
try:
    print(x)
except NameError:
    print("Variable x not defined")
finally:
    print("Completed")
print("\n") #Empty Space


#Exception Raise
x = -1
if x < 0:
    raise Exception("No negative numbers")
print("\n") #Empty Space


#TypeError
x = "Hello "
if not type(x) is int:
    raise TypeError("Only Integers, Sorry")
print("\n") #Empty Space

print("\nEND OF TRY/EXCEPT LESSON\n\n") #End of try/except Lesson