# Basic While/For Loops of Python - May 19, 2022
# Written by V I E R U S
# While Loops: creating a while loop, Break, Continue, While else 
# For loop: Created a loop, Loop through a string, Break, Continue, Range, For Loop, Nested Loop
# Variables: myArray, myArray2
from ast import Continue

#While Loops-------------------------------------------------------
#Can be Executed as long as its true
#Creating a While Loop


i =2
while i < 10:
    print(i)
    i+=1
print("\n") #Empty Space


#BREAK
while i < 10:
    print(i)
    if i == 7:
        break
    i+=1
print("\n") #Empty Space


#CONTINUE
while i < 10:
    i+=1
    if i == 7:
        continue
    print(i)
print("\n") #Empty Space


#While Else
while i < 10:
    print(i)
    i+=1
else:
    print("i is no longer less than 10")
print("\n") #Empty Space


#For Loops----------------------------------------------------------
#Creating a for loop
myArray = ["Cat", "Dog", "Fish"]
for x in myArray:
    print(x)
print("\n") #Empty Space


#Loop through String
for x in "Fish":
    print(x)
print("\n") #Empty Space


#BREAK
for x in myArray:
    print(x)
    if x == "Dog":
        break
print("\n") #Empty Space


#CONTINUE
for x in myArray:
    if x == "Dog":
        Continue
    print(x)
print("\n") #Empty Space


#Range
for x in range(2):
    print(x)
print("\n") #Empty Space


#For Else 
for x in range(2):
    print(x)
else:
    print("Completed")
print("\n") #Empty Space


#Nested Loop
myArray2 = ["Red", "Blue", "Yellow"]
for x in myArray2:
    for y in myArray:
        print(x, y)
print("\n") #Empty Space


print("\nEND OF WHILE/FOR LOOP LESSON\n\n") #End of While/For Loop Lesson