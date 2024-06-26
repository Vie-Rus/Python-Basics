# Python Basics
Written by V I E R U S in python

# Basic Methods---------------------------------------------
    This program goes into the very basics of python. This includes: 
        - Array: create an array, access elements, Change/Add Items, Length, Loop Array, removing items by pop/remove, Reverse an array

        - Dictionaries: Creating a dictionary, call specific items, length, data type, find variable by calling on it/get, get keys by get key/key exist, get value, get item, changing or adding value by add/update, removing value by pop/popitem/del/clear, for loop: key one by one/key method/value one by one/value method/both keys and value using item, copy list using copy/dict, nested dictionary

        - Def Functions: using variable 32, explains how a function works, value inside the def vs outside the def is different

        - Multi-Variables: using variables 4-13, Multi-Line string, string array, many values to many variables, one value to many variables, and unpacking a list
    
        - String: using variables 14-21, String length, check if a letter/word is in the sentence or not, String slice at start/end/negative index, Capitalize/Lower case a string, Remove spaces at beginning and end, Split String, Replace letters in a string, String format, having quotes in a string 
    
        - Math/Numbers: 
            - Using variables 22-31 | import math/random, shows int, float, scientific number, complex numbers (Imaginary), random numbers, finding the min and max values, Adding a power to something, Squaring something, Ceil - rounding up, Floor - rounding down
    
            - Boolean: REUSING variables 18 and 20, explains how a boolean works, basically a true or false
    
            - Date: using variables 33-34 | import datetime, shows how to set a date, weekdays, months, local date/time, and month as a number
    
        - User Input: shows how to let the user give an input

        - Lists: Creating one, Find length, Type, Constructors, access certain item in the list, check if item is in list, Change item in list, add to list, Iterable/Extend list, remove list items, pop/delete/clear, Loops, sort/descend, copy, join list regardless of types.

        - Tuples: Create a tuple, find length, types, join, contructor, index, change something in tuple, Append/Remove, Loops
        
        - Sets: Creating a set, length, data type, constructor, access item, check item, add/update, Union/Update, Remove/Discard/Pop/Clear/Del, for loop, Keep/Remove Duplicates 
        
        - If/Else: If/Else: created an If/Else, Shorthand for If/ELIF/Else, AND, OR, Nested If, variable var1-3
        
        - While/For Loops: creating a while loop, Break, Continue, While else / Created a for loop, Loop through a string, Break, Continue, Range, For Loop, Nested Loop, variable myArray, myArray2

        - Functions: created a function, used arguments/parameters, *args, default parameter value, Pass a list/For loop, return value, variables myFunction0-5
        
        - Lambda: Creating a lambda, add multiple values, double/triple/etc your value, Variables var1-3, doubleIt
        
        - Arrays: Creating an Array, access elements, change item, add item, length, for loop, removing using Pop/Remove, variable var1, var2, pets
        
        - Try/Except: Created a try/except, NameError, Else Loop, Final, Raise Exception, TypeError

        - Classes/Object: Create a class/object, __init__() function = MyClass1, Object Method = MyClass2, Modify object properties, delete object 
        
        - Inheritance: create an inheritance of parent and child class = MyClass3, puts variables in parent and child class 
        
        - Iterator: Created a string iterator which goes through each letter, created Loop string iterator, Created a tuple iterator which goes through each word, created loop tuple iterator, Created a class/object itertor that would only loop until 5 and then stops
        
        - Scope: Local scope, calls function within a function, global scope > go back to python basic function for understanding, global keyword to make variable global

# Python Tkinter------------------------------------------
    Basics.py
        This program opens a GUI in tinker that has a series of tabs that go over the basics within tkinter
        
        Frame 1: Labels, Buttons, Entry, Check boxes, Radio boxes, Drop-Down boxes. 
            - Labels: Creating a label and explaing how grid works. Pack shoves the code onto the screen and automatically resizes. Grid will let you organize more, but will not resize.

            - Buttons: Creating a button, how to use state to disable a button, make a button a wacky size using padx/pady, how to make a button have an action using def, changed color of font/button within the button.
            NOTE: mybut9 and mybut10 variable are used in Entry.

            - Entry: Creating an entry, making the entry background a color, creating a border width, def Entry get will return output, Entry insert will insert text within the entry box already
    
            - Check Boxs: Creating a check box, created variables for amount of boxes, def isChecked shows variable output
    
            - Radio Buttons: Creating a radio button, created a variable (1) for radio variables, def radioClick shows what you selected
    
            - Drop-Down Buttons: Creating a drop-down box, created a variable (1) for dropbox to remember your input, set dropbox to value
        
        Frame 2: LabelFrames
            How to label and section off certain information along with next and prev tab buttons. These next and prev tab buttons uses .select(framenumber)
            - LabelFrame: 

        Frame 3: File
            from tkinter import filedialog
            - File: 

        Frame 4: New Window Tab
            - New Window: using a def you can call upon topLevel() to open a second window and add whatever you want from it. Different than Messagebox, topLevel does not come with pre-determined buttons, certain sounds and images.

        Frame 5: Insert an Image
            from PIL import ImageTK, Image
            - Image: to inset an image you have to use .PhotoImage

        Frame 6: MessageBoxes
            from tkinter import messagebox
            - MessageBox: there are a series of messageboxes to pick from. value:button labels
                .showinfo        ||  shows 'I-circle' image, returns ok:okay
                .showwarning     ||  shows '!-triangle' image, returns ok:okay
                .showerror       ||  shows 'x-circle' image, returns ok:okay
                .askquestion     ||  shows '?-circle' image, returns returns yes:yes, no:no
                .askokcancel     ||  shows '?-circle' image, returns 1:Okay, 0:Cancel
                .askyesno        ||  shows '?-circle' image, returns 1:yes, 0:no
                .askyesnocancel  ||  shows '?-circle' image, returns 1:yes, 0:no, closes popup:cancel
                .askretrycancel  ||  shows '!-triangle' image, returns 1:retry, 0:cancel


    Image_status.py
        This is an image viewer program, that allows you to view a set of images, 4. You can press the Next button '>>', previous button '<<', or exit button to leave the program.
        The images come from the image folder
        

# File Folder---------------------------------------
        - A CSV and Text file are already added to the file to help with any data you may need in files.py and WithOpen.py
            CVSFile.cvs
            TextFile.txt
        
        - WithOpen.py
            This program goes into the basics of how to open a text/cvs file. Uses loops to read the files.
        
        - Files.py
            Section 1 goes into the different ways to read a file, 
            Section 2 goes into writing data to the file, 
            Section 3 goes into creating a new file and deleting a file. 

