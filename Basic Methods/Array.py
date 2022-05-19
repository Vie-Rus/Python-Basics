# Basic Array of Python - May 19, 2022
# Written by V I E R U S
# Array: Creating an Array, access elements, change item, add item, length, for loop, removing using Pop/Remove
# Variables: var1, var2, pets

#Array-----------------------------------------------------------
#Created an array
pets = ["Cat", "Dog", "Fish"]

#access elements
var1 = pets[0]
print(var1)
print("\n") #Empty Space


#Change item
pets[2] = "Horse"
print(pets)
print("\n") #Empty Space


#Add item
pets.append("Fish")


#length of array
var2 = len(pets)
print(var2)
print("\n") #Empty Space

#Loop Array
for x in pets:
    print(x)
print("\n") #Empty Space


#Removing item by Pop/Remove
    #Pop
pets.pop() #Removes last item
print(pets)
print("\n") #Empty Space


    #Remove
pets.remove("Horse") #Removes specific item
print(pets)
print("\n") #Empty Space


#Reverses
pets.reverse()
print(pets)
print("\n") #Empty Space


print("\nEND OF ARRAY LESSON\n\n") #End of array Lesson