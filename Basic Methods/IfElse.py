# Basic If/Else of Python - May 19, 2022
# Written by V I E R U S
# If/Else: created an If/Else, Shorthand for If/ELIF/Else, AND, OR, Nested If
# Variables: var1-3 

#If/Else-----------------------------------------------------------------
var1 = 100
var2 = 45
if var1 > var2:
    print("Var1 is greater than Var2")
elif var1 == var2:
    print("They are equal to one another")
else:
    print("Var 2 is greater")
print("\n") #Empty Space


#short hand for If
if var1 > var2: print("var1 is greater than var2")
print("\n") #Empty Space


#short hand for If/Else
print("var1") if var1 > var2 else print("var2")
print("var1") if var1 > var2 else print("var2")
print("\n") #Empty Space


#AND
var3 = 78
if var1 > var2 and var3 > var1:
    print("Both are true")
else:
    print("This is false")
print("\n") #Empty Space


#OR
if var1 > var2 or var3 > var1:
    print("One is true")
print("\n") #Empty Space


#Nested If
Var2= 45
if var2 > 40:
    print("Higher, ")
    if var2 < 50:
        print("Lower, ")
    else:
        print("Its 45")
print("\n") #Empty Space

print("\nEND OF IF/ELSE LESSON\n\n") #End of if/else Lesson