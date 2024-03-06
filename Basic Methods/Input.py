# Basics of Python - March 29, 2022
# Written by V I E R U S
#User input----------------------------------------------------------
userInput = input("Enter anything my dude: ")
print("You Entered: " + userInput +"\n")
print("\n") #Empty Space

UserInput2 = input("Enter multiple values with a space in between: ")
userValue = UserInput2.split()
user1 = userValue[0]
user2 = userValue[1]
print("Your first value was: " + user1 + "Your second value was: " + user2)
print("\n") #Empty Space