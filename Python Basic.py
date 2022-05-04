


#Print (var1-3)-------------------------------------------
print("Start Basics\n")

#Print values
var1 = 45
print(var1, " : This is the value of 45\n")


#Casting
var2 = str(3)
var3 = int(2)
print(var2, var3 , " : results should be 3 and 2\n")


#Get Type,
print(type(var2))
print(type(var1))



#Multi Variables (var4-13)--------------------------------------------------------
#Multi-Line String
var4 = """The Quick,
Brown Fox ran
down the hill fast """
print(var4)


#String Array 
print(var4[7]+ " : value should be c\n")


#Many values, many variable
var5, var6, var7 = "Dog", "Fish", "Cat"
print(var6, var7, var5, " : Value should be Fish, Cat, Dog\n")


#One value, many variable
var8 = var9 = var10 = "Circle"
print(var9)
print(var8)
print("Circle prints twice\n")


#unpacking a list
colors = ['blue', 'red', 'yellow']
var11, var12, var13 = colors
print(var11, var12, var13, " : Value Blue, Red, Yelllow")



#Strings (var 14-21)-------------------------------------------------------------------
#String Length
var14 = "This is a lot of lines of code so far haha"
print(len(var14), " : The value should be 41 or 42")


#String Check if there or not 
var15 = "After the Storm hit the peach rings They Fought"
print("Fought" in var15, " : Value is true")
if "rings" in var15:
    print("THE RINGS ARE MINE\n")
    
#or not
print("the" not in var15, " : Value is false")
if "He" not in var15:
    print("No Genders here Zir lol\n")


#String Slice
var16 = "Angel Sniffs"
print(var16[3:7], " : Value should be el S \n")

#from start
print(var16[:7], " : Value should be Angel S \n")

#from end
print(var16[3:], " : Value should be el Sniffs \n")

#Negative Indexing
print(var16[-7:-3], " : Value should be Sni \n")


#String Upper
print(var16.upper(), " : Value should be ANGEL SNIFFS \n")

#String Lower
print(var16.lower(), " : Value should be angel sniffs \n")


#String, no spaces beginning and ending
var17 = " Already on Tee "
print(var17.strip(), " : Value should be 'Already on Tee' \n")

#String Split
var17 = " Already, on, Tee "
print(var17.split(","), " : Value should be ['Already', 'on', 'Tee'] \n")

#String Replace
print(var17.replace("T", "S") , " : Value should be Already on See \n")

#String Format
var18 = 23
var19 = "socks"
var20 = 16.605
var21 = "My age is {1}, i eat {2}, i paid {0}"
print(var21.format(var20, var18, var19), " : Value should be My age is 23, i eat socks, i paid 16.605 \n")

var21 = "My age is {}, i eat {}, i paid {:.2f}"
print(var21.format(var18, var19, var20), " : Value should be My age is 23, i eat socks, i paid 16.61 \n")

var21 = "My age is {1}, i eat {2}, i paid {0:.2f}"
print(var21.format(var20, var18, var19), " : Value should be My age is 23, i eat socks, i paid 16.61 \n")

var21 = "My age is {u1}, i eat {w2}, i paid {0:.2f}"
print(var21.format(var20, u1 = 69, w2 = "Smutt"), " : Value should be My age is 69, i eat Smutt, i paid 16.61 \n")


#String Quotes
print("This is how you \"add quotes\" in a sentence\n")
print()


#Math/Numbers (var 22-31)---------------------------------------------------------------------------------------------------------
import math

var22 = 1 #int
var23 = 2.2 #float
var24 = 2.2e2 #float,can be scientific number wtih 'E' or 'e'
var25 = 3j #complex, 'j' as imaginary part

#Random Numbers
import random
print(random.randrange(1,10), " : random value")

var26 = min(0,2,4,6,8)
var27 = max(1,3,5,7,9)
print (var26, var27, " : Values should be 0, 9")

    #power
var28 = pow(5,6)
print(var28, ": Value should be 15625")

    #square
var29 = math.sqrt(64)
print(var29)

#Ceil: rounds up
var30 = math.ceil(4.4)
#Floor: rounds down
var31 = math.floor(4.4)
print(var30, var31, ": Values should be 5, 4")



#Boolean (REUSES var 18 and 20)--------------------------------------------------------------
print(bool("Hello"))
print(bool())

#Boolean Function
def mybool():
    #var18 = 23
    #var20 = 16.605
    if var18 < var20:
        return True

if mybool():
    print("CORRECT")
else:
    print("WRONG WRONG WRONG")

#Boolean isinstance()
print(isinstance(var18, int))
print()



#Date (var 33-34)------------------------------------------------------------------
import datetime
var33 = datetime.datetime.now()
var34 = datetime.datetime(2022, 4, 12)
print(var33)

#Date strftime()
print(var34.strftime("%A"), ": Weekday Long") # a -> weekday short
print(var34.strftime("%B"), ": Month Long") # b -> Month short
print(var34.strftime("%c"), ": local version of date and time")
print(var34.strftime("%m"), ": Month as a number") # M -> Minutes 00-59



#Def Functions (var 32 )-------------------------------------------------------
var32 = "kitten"
def myfunc():
    var32 = "Kilt"
    print("Kilt should be this value : " + var32)
myfunc()
print("Kitten should be this value : " + var32)
print()



#User input----------------------------------------------------------
userInput = input("Enter anything my dude: ")
print("You Entered: " + userInput +"\n")