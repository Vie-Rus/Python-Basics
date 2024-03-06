# Basics of Python - March 29, 2022
# Written by V I E R U S

#Print (var1-3)-------------------------------------------
print("Start Basics\n")

#Print values
var1 = 45
print(var1, " : This is the value of 45\n")
print("\n") #Empty Space

#Casting
var2 = str(3)
var3 = int(2)
print(var2, var3 , " : results should be 3 and 2\n")
print("\n") #Empty Space

#Get Type,
print(type(var2))
print(type(var1))
print("\n") #Empty Space

#Multi Variables (var4-13)--------------------------------------------------------
#Multi-Line String
var4 = """The Quick,
Brown Fox ran
down the hill fast """
print(var4)
print("\n") #Empty Space

#String Array 
print(var4[7]+ " : value should be c\n")
print("\n") #Empty Space

#Many values, many variable
var5, var6, var7 = "Dog", "Fish", "Cat"
print(var6, var7, var5, " : Value should be Fish, Cat, Dog\n")
print("\n") #Empty Space

#One value, many variable
var8 = var9 = var10 = "Circle"
print(var9)
print(var8)
print("Circle prints twice\n")
print("\n") #Empty Space

#unpacking a list
colors = ['blue', 'red', 'yellow']
var11, var12, var13 = colors
print(var11, var12, var13, " : Value Blue, Red, Yelllow")
print("\n") #Empty Space



#Strings (var 14-21)-------------------------------------------------------------------
#String Length
var14 = "This is a lot of lines of code so far haha"
print(len(var14), " : The value should be 41 or 42")
print("\n") #Empty Space

#String Check if there or not 
var15 = "After the Storm hit the peach rings They Fought"
print("Fought" in var15, " : Value is true")
if "rings" in var15:
    print("THE RINGS ARE MINE\n")
print("\n") #Empty Space
    
#or not
print("the" not in var15, " : Value is false")
if "He" not in var15:
    print("No Genders here Zir lol\n")
print("\n") #Empty Space

#String Slice
var16 = "Angel Sniffs"
print(var16[3:7], " : Value should be el S \n")
print("\n") #Empty Space

#from start
print(var16[:7], " : Value should be Angel S \n")
print("\n") #Empty Space

#from end
print(var16[3:], " : Value should be el Sniffs \n")
print("\n") #Empty Space

#Negative Indexing
print(var16[-7:-3], " : Value should be Sni \n")
print("\n") #Empty Space

#String Upper
print(var16.upper(), " : Value should be ANGEL SNIFFS \n")
print("\n") #Empty Space

#String Lower
print(var16.lower(), " : Value should be angel sniffs \n")
print("\n") #Empty Space

#String, no spaces beginning and ending
var17 = " Already on Tee "
print(var17.strip(), " : Value should be 'Already on Tee' \n")
print("\n") #Empty Space

#String Split
var17 = " Already, on, Tee "
print(var17.split(","), " : Value should be ['Already', 'on', 'Tee'] \n")
print("\n") #Empty Space

#String Replace
print(var17.replace("T", "S") , " : Value should be Already on See \n")
print("\n") #Empty Space

#String Format
var18 = 23
var19 = "socks"
var20 = 16.605
var21 = "My age is {1}, i eat {2}, i paid {0}"
print(var21.format(var20, var18, var19), " : Value should be My age is 23, i eat socks, i paid 16.605 \n")
print("\n") #Empty Space

var21 = "My age is {}, i eat {}, i paid {:.2f}"
print(var21.format(var18, var19, var20), " : Value should be My age is 23, i eat socks, i paid 16.61 \n")
print("\n") #Empty Space

var21 = "My age is {1}, i eat {2}, i paid {0:.2f}"
print(var21.format(var20, var18, var19), " : Value should be My age is 23, i eat socks, i paid 16.61 \n")
print("\n") #Empty Space

var21 = "My age is {u1}, i eat {w2}, i paid {0:.2f}"
print(var21.format(var20, u1 = 69, w2 = "Smutt"), " : Value should be My age is 69, i eat Smutt, i paid 16.61 \n")
print("\n") #Empty Space

#String Quotes
print("This is how you \"add quotes\" in a sentence\n")
print("\n") #Empty Space

