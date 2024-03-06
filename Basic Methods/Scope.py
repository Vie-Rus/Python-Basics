# Basic Classes Related - 
# Written by V I E R U S
# Classes/Object, Inheritance, Iterator, Scope
# Variables: var1-10
# Scope-------------------------------------------------------
# variable only available from inside the region

#local Scope
def scopeFunc():
    var8 = 300
    print(var8)

scopeFunc()
print("\n") #Empty Space


#Function inside Function
def scopeFunc1():
    var9 = 200
    def innerScopeFunc():
        print(var9)
    innerScopeFunc()
scopeFunc1()
print("\n") #Empty Space

#Global Scope - variable outside function used by anyone > Python Basic Function
#Global Keyword - makes variable global

def scopeFunc2():
    global var10
    var10 = 100
    
scopeFunc2()
print(var10) # 100 Prints here
print("\n") #Empty Space 
