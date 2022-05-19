# Basic Functions of Python - May 19, 2022
# Written by V I E R U S
# Sets: Creating a set, length, data type, constructor, access item, check item, add/update, Union/Update, Remove/Discard/Pop/Clear/Del, for loop, Keep/Remove Duplicates 
# Variables: mySet, mySet2, mySet3, mySet4

#Sets----------------------------------------------------------------------------
#Set is collection which unordered/unchangeable, unindexed, no duplicates
#Creating a set
mySet = {"Cat", "Dog", "Fish"}
print(mySet)
print("\n") #Empty Space


#No Duplicates
mySet = {"Cat", "Dog", "Fish", "Cat"}
print(mySet)
print("\n") #Empty Space


#length
mySet = {"Cat", "Dog", "Fish"}
print(len(mySet))
print("\n") #Empty Space


#Data Type
mySet = {"Cat", "Dog", "Fish"}
mySet2 = {3, 2, 1}
mySet3 = {True, False, False}
mySet4 = {"Horse", 65, False}
print(type(mySet4))
print("\n") #Empty Space


#Constructor
ConstructorSet = mySet(("Hamster", "Dog", "Fish"))
print(ConstructorSet)
print("\n") #Empty Space


#Access Items
mySet = {"Cat", "Dog", "Fish"}
for x in mySet:
    print(x)
print("\n") #Empty Space
    
    
#Check Items
print("Dog" in mySet)
print("\n") #Empty Space


#Add Items by add or update
    #add
mySet = {"Cat", "Dog", "Fish"}
mySet.add("Hamster")
print(mySet)
print("\n") #Empty Space


    #update - Can add a list onto a set as well using update
mySet = {"Cat", "Dog", "Fish"}
mySet2 = {"Red", "Blue", "Yellow"}
mySet.update(mySet2)
print(mySet)
print("\n") #Empty Space


#join - Union/update(above)
    #Union
mySet = {"Cat", "Dog", "Fish"}
mySet2 = {3, 2, 1}
mySet3 = mySet.union(mySet2)
print(mySet3)
print("\n") #Empty Space


#Remove/Discard/Pop/Clear/Del
    #remove
mySet = {"Cat", "Dog", "Fish", "Horse", "Hamster", "Goat"}
mySet.remove("Fish")
print(mySet)
print("\n") #Empty Space


    #discard
mySet.discard("Dog")
print(mySet)
print("\n") #Empty Space
    
    
    #pop
mySet.pop()
print(mySet)
print("\n") #Empty Space


    #clear
mySet.clear()
print(mySet)
print("\n") #Empty Space


    #del
mySet = {"Cat", "Dog", "Fish", "Horse", "Hamster", "Goat"}
del mySet
print(mySet)
print("\n") #Empty Space


#ONLY for loops works on sets
mySet = {"Cat", "Dog", "Fish", "Horse", "Hamster", "Goat"}
for x in mySet:
    print(x)
print("\n") #Empty Space
    
    
#Duplicates
    #intersection update - Keep only Duplicates
mySet = {"Cat", "Dog", "Fish"}
mySet2 = {"Red", "Blue", "Dog"}
mySet.intersection_update(mySet2)
print(mySet)
print("\n") #Empty Space


    #intersection - return a new set
mySet = {"Cat", "Dog", "Fish"}
mySet2 = {"Red", "Blue", "Dog"}
mySet3 = mySet.intersection(mySet2)
print(mySet3)
print("\n") #Empty Space


    #Symmetric_difference_updates - Doesn't keep duplicates
mySet = {"Cat", "Dog", "Fish"}
mySet2 = {"Red", "Blue", "Dog"}
mySet.symmetric_difference_update(mySet2)
print(mySet)
print("\n") #Empty Space


    #Symmetric_difference - return a new set, doesn't keep duplicates
mySet = {"Cat", "Dog", "Fish"}
mySet2 = {"Red", "Blue", "Dog"}
mySet3 = mySet.intersection(mySet2)
print(mySet3)
print("\n") #Empty Space

print("\nEND OF SETS LESSON\n\n") #End of Set Lesson