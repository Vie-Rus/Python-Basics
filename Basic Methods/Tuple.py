# Basic Functions of Python - May 15, 2022
# Written by V I E R U S
# Tuples: Create a tuple, find length, types, join, contructor, index, change something in tuple, Append/Remove, Loops
# Varibles used: myTuple, myTuple2, singleTuple, ComboTuple, xTuple, yTuple

#Tuples---------------------------------------------------------------------------------------
#unchangeable order, starts at 0 > Index
myTuple = ("Cat", "Dog", "Fish","Horse", "Froggie")
print(myTuple)
print("\n") #Empty Space


#Only one tuple needs a comma at the end
singleTuple = ("Cat",)
print(type(singleTuple))
print("\n") #Empty Space


#different data types
myTuple2 = ("Snake", 123, False, 987)


#Find Length
print(len(myTuple))
print("\n") #Empty Space


#join Tuples
ComboTuple = myTuple + myTuple2
print(ComboTuple)
print("\n") #Empty Space


#constructor
myTuple3 = tuple(("Cat", "Dog", "Fish"))
print(myTuple3)
print("\n") #Empty Space


#index
print(myTuple2[2] + " : False")
print("\n") #Empty Space


#change tuple > convert into a list then into a tuple
xTuple = ("Cat", "Dog", "Fish")
yTuple = list(xTuple)
yTuple[1] = "Horse"
xTuple = tuple(yTuple)
print(xTuple)
print("\n") #Empty Space


#Append/Remove tuple > convert into a list then into a tuple or tuple + tuple (APPEND ONLY)
yTuple = list(xTuple)
yTuple.append("Horse")  #yTuple.remove("Dog")
xTuple = tuple(yTuple)
print(xTuple)
print("\n") #Empty Space


#Tuple Loops
for x in myTuple2:
    print(x)
print("\n") #Empty Space


#index Loop
for i in range(len(myTuple2)):
    print(myTuple2[i])
print("\n") #Empty Space

    
#while Loop
i=0
while i < len(myTuple2):
    print(myTuple2[i])
    i =+ 1
print("\n") #Empty Space
print("\nEND OF TUPLE LESSON\n\n") #End of Tuple Lesson