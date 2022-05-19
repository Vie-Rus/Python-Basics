# Basic Dictionaries of Python - May 19, 2022
# Written by V I E R U S
# Dictionary: Creating a dictionary, call specific items, length, data type, find variable by calling on it/get, get keys by get key/key exist, get value, get item, changing or adding value by add/update, removing value by pop/popitem/del/clear, for loop: key one by one/key method/value one by one/value method/both keys and value using item, copy list using copy/dict, nested dictionary 
# Variables: myDict, myDict2, var1, var2, var3, petDict, petDict2, petDict3, VetDict

#Dictionary------------------------------------------------------
#Changeable, no Duplicates
#Creating a dict
myDict = { "Color": "Brown",
          "Breed": "Cat",
          "Owner ID": 1234 
          }
print(myDict)
print("\n") #Empty Space

#Call specific item
print(myDict["Owner ID"])
print("\n") #Empty Space


#length
print(len(myDict))
print("\n") #Empty Space


#Data types: String/Int/Boolean/List
#Type
print(type(myDict))
print("\n") #Empty Space


#Value of Model key variable/get
    #Variable 
var1 = myDict["Color"]
print(var1)
print("\n") #Empty Space


    #Get
var1 = myDict.get("Breed")
print(var1)
print("\n") #Empty Space


#Keys - Get key/Key Exist
    #get Keys
var2 = myDict.keys()
print(var2)
print("\n") #Empty Space


    #Key Exist
if "Breed" in myDict:
    print("Yes there are Breeds in this Dictionary")
print("\n") #Empty Space


#Get Values
var3 = myDict.values()
print(var3)
print("\n") #Empty Space


#Get Items
var3 = myDict.items()
print(var3)
print("\n") #Empty Space


#Change/Adding Values by Add/Update
    #Add
myDict["Breed"] = "Dog"


    #Update
myDict.update({"Owner ID": 9876})
print(myDict)
print("\n") #Empty Space


#Removing Values by Pop/PopItem/del/clear
    #Pop
myDict.pop("Owner ID")

    #PopItem - removes last inserted item
myDict.popitem()
print(myDict)
print("\n") #Empty Space

    #del - will delete existing dictionary 
#del myDict

    #Clear
myDict.clear()
print(myDict)
print("\n") #Empty Space


#For Loop
myDict = { "Color": "Brown",
          "Breed": "Cat",
          "Owner ID": 1234 
          }

    #Print Key Names one by one
for x in myDict:
    print(x)
print("\n") #Empty Space

    #or use keys method
for x in myDict.keys():
    print(x)
print("\n") #Empty Space


    #Print all Values one by one
for x in myDict:
    print(myDict[x])
print("\n") #Empty Space

    #or use values method
for x in myDict.values():
    print(x)
print("\n") #Empty Space


    #Both Keys and Values by using Item Method
for x, y in myDict.items():
    print(x,y)
print("\n") #Empty Space


#Copy using Copy/Dict
    #Copy
myDict2 = myDict.copy()
print(myDict2)
print("\n") #Empty Space

    #Dict
myDict2 = dict(myDict)
print(myDict2)
print("\n") #Empty Space

#Nested - Dictionary that contains three dictionary
petDict = {
     "Breed": "Cat",
     "Owner ID": 1234
    }
petDict2 = {
     "Breed": "Dog",
     "Owner ID": 9876
    }
petDict3 = {
     "Breed": "Fish",
     "Owner ID": 4200
    }

VetDict = {
    "petDict": petDict,
    "petDict2": petDict2,
    "petDict3": petDict3,
}

print("\n") #Empty Space
print("\nEND OF DICTIONARY LESSON\n\n") #End of Dictionary Lesson