# Basics of Python - March 29, 2022
# Written by V I E R U S
#Math/Numbers (var 22-31)---------------------------------------------------------------------------------------------------------
import math

var22 = 1 #int
var23 = 2.2 #float
var24 = 2.2e2 #float,can be scientific number wtih 'E' or 'e'
var25 = 3j #complex, 'j' as imaginary part

#Random Numbers
import random
print(random.randrange(1,10), " : random value")
print("\n") #Empty Space

var26 = min(0,2,4,6,8)
var27 = max(1,3,5,7,9)
print (var26, var27, " : Values should be 0, 9")
print("\n") #Empty Space

    #power
var28 = pow(5,6)
print(var28, ": Value should be 15625")
print("\n") #Empty Space

    #square
var29 = math.sqrt(64)
print(var29)
print("\n") #Empty Space

    #Ceil: rounds up
var30 = math.ceil(4.4)

    #Floor: rounds down
var31 = math.floor(4.4)
print(var30, var31, ": Values should be 5, 4")
print("\n") #Empty Space

#Boolean (REUSES var 18 and 20)--------------------------------------------------------------
print(bool("Hello"))
print(bool())
print("\n") #Empty Space

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
print("\n") #Empty Space

#Boolean isinstance()
print(isinstance(var18, int))
print()
print("\n") #Empty Space

#Date (var 33-34)------------------------------------------------------------------
import datetime
var33 = datetime.datetime.now()
var34 = datetime.datetime(2022, 4, 12)
print(var33)
print("\n") #Empty Space

#Date strftime()
print(var34.strftime("%A"), ": Weekday Long") # a -> weekday short
print(var34.strftime("%B"), ": Month Long") # b -> Month short
print(var34.strftime("%c"), ": local version of date and time")
print(var34.strftime("%m"), ": Month as a number") # M -> Minutes 00-59
print("\n") #Empty Space