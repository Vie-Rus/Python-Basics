# Basic Functions of Python - May 5, 2022
# Written by V I E R U S
# Lists: Creating one, Find length, Type, Constructors, access certain item in the list, check if item is in list,
# Change item in list, add to list, Iterable/Extend list, remove list items, pop/delete/clear, Loops, sort/descend, copy, join list regardless of types
# Variables: myList, myList2, myList3

#Lists------------------------------------------------------------------------------------------------
#Creating a list
myList = ["a", "b", "c", "d", "e", "f", "g"]
print(myList, " : This value should be a b c d e f g\n")
print("\n") #Empty Space


#List Length, Doesn't start at 0
print(len(myList), ": This value should be 7\n")
print("\n") #Empty Space


#Type()
print(type(myList), ": This value should be <Class 'List'>\n")
print("\n") #Empty Space


#List() Contructor
myList2 = list(("a1", "b1", "c1" ))
print(myList2)
print("\n") #Empty Space


#Access Certain Items
#starts with 0
print(myList[1], ": This value should be - b\n")
print("\n") #Empty Space


#-1 starts at end
print(myList[-1], ": This value should be - g\n")
print("\n") #Empty Space


#prints between the numbers you request
print(myList[1:4], ": This value should be - b c d\n")
print("\n") #Empty Space


#print start to before end number
print(myList[:4], ": This value should be - a b c d\n")
print("\n") #Empty Space


#print before start to end
print(myList[2:], ": This value should be - c d e f g\n")
print("\n") #Empty Space


#Check if Item exist
if "e" in myList:
    print("yes, e is in the list.\n")
else:
    print("No, its not in the list\n")
print("\n") #Empty Space


#Change List Items
myList[0] = "z"
print(myList, ": value should be z b c d e f g\n")
print("\n") #Empty Space

myList[1:3] = ["y", "x"]
print(myList, ": This value should be z y x d e f g\n")
print("\n") #Empty Space

myList.insert(-1, "a")
print(myList, ": This value should be z y x d e f a g\n")
print("\n") #Empty Space


#Add List
myList.append("b")
print(myList, ":This value will be - z y x d e f a g b\n")
print("\n") #Empty Space


#Iterable/Extend list
myList.extend(myList2)
print(myList)
print("\n") #Empty Space


#Remove List Items - Remove/Pop/Delete/Clear
    #Remove
myList.remove("g")
print(myList, ":This value will be - z y x d e f a b c1\n")
print("\n") #Empty Space


    #Pop
myList.pop()
print(myList, ":This value will be - z y x d e f a b\n")
print("\n") #Empty Space


    #Delete
del myList[0]
print(myList, ":This value will be - y x d e f a b\n")
print("\n") #Empty Space


    #Clear list
myList.clear()
print(myList)
print("\n") #Empty Space


#Loop List
myList = ["a", "b", "c", "d", "e", "f", "g"]
for x in myList:
    print(x)
print("\n") #Empty Space


#Short hand for Loop lists
[print(x) for x in myList]
print("\n") #Empty Space


#Loop List by Index
for i in range(len(myList)):
    print(myList[i])
print("\n") #Empty Space


#While loop
i = 0
while i < len(myList):
    print(myList[i])
    i += 1
print("\n") #Empty Space


#Sort alphabetically/numerically
myList2 = [234, 234, 56, 23, 2, 9234]
myList2.sort()


#Descend alphatically/numerically
myList3 = ["Fish", "Dog", "Cat", "Horse"]
myList3.sort(reverse = True)
print(myList2 + "\n\n" + myList3)
print("\n") #Empty Space


#Copy list
petList = list(myList3)
print(petList)
print("\n") #Empty Space


#Join List regardless of types
ComboList = myList2 + myList3
print(ComboList)
print("\n") #Empty Space


print("\nEND OF LIST LESSON\n\n") #End of List Lesson