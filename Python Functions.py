# Basic Functions of Python - April 1, 2022
# Written by V I E R U S
# Lists, Tuples, Sets, Dictionaries, If/Else, While Loops,
# For Loops, Functions, Lambda, Arrays, Try/Except

#Lists---------------------------------------------------------------

myList = ["a", "b", "c", "d", "e", "f", "g"]
print(myList, " : This value should be a b c d e f g\n")

    #List Length, Doesn't start at 0
print(len(myList), ": This value should be 7\n")

    #Type()
print(type(myList), ": This value should be <Class 'List'>\n")

    #List() Contructor
myList2 = list(("a1", "b1", "c1" ))
print(myList2)

    #Access Certain Items
#starts with 0
print(myList[1], ": This value should be - b\n")

#-1 starts at end
print(myList[-1], ": This value should be - g\n")

#prints between the numbers you request
print(myList[1:4], ": This value should be - b c d\n")

#print start to before end number
print(myList[:4], ": This value should be - a b c d\n")

#print before start to end
print(myList[2:], ": This value should be - c d e f g\n")

#Check if Item exist
if "e" in myList:
    print("yes, e is in the list.\n")
else:
    print("No, its not in the list\n")

    #Change List Items
myList[0] = "z"
print(myList, ": value should be z b c d e f g\n")

myList[1:3] = ["y", "x"]
print(myList, ": This value should be z y x d e f g\n")

myList.insert(-1, "a")
print(myList, ": This value should be z y x d e f a g\n")

#Add List
myList.append("b")
print(myList, ":This value will be - z y x d e f a g b\n")

#Iterable/Extend list
myList.extend(myList2)
print(myList)

    #Remove List Items
myList.remove("g", "a1", "b1")
print(myList, ":This value will be - z y x d e f a b c1\n")

    #Pop
myList.pop()
print(myList, ":This value will be - z y x d e f a b\n")

    #delete
del myList[0]
print(myList, ":This value will be - y x d e f a b\n")

    #clear list
    #del myList
myList.clear()
print(myList)

#Loop List
myList = ["a", "b", "c", "d", "e", "f", "g"]
# for f in myList:
#     print(x)

#short hand
[print(x) for x in myList]

#Loop List by Index
for i in range(len(myList)):
    print(myList[i])




#Tuples--------------------------------------------------------------


# Sets---------------------------------------------------------------


# Dictionaries------------------------------------------------------- 


# If/Else------------------------------------------------------------


# While Loops--------------------------------------------------------


# For Loops----------------------------------------------------------


# Functions----------------------------------------------------------


# Lambda-------------------------------------------------------------


# Arrays------------------------------------------------------------- 


# Try/Except---------------------------------------------------------


