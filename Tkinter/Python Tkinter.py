#imports
from ast import Lambda
from cProfile import label
from multiprocessing import Value
from struct import pack
from tkinter import *

#Creates a GUI in python that goes into Labels, Buttons, Entry, Radio Buttons, 
# Check boxes, Drop down boxes, and menu bar

def labelWin():
    labelWindow = Toplevel()
    labelWindow.geometry("600x600")
    labelWindow.title("Label's Window")
    #Creating a label-----------------------------------------------------
    mylab1 = Label(labelWindow, text="Intro") 
    mylab2 = Label(labelWindow, text="This is the basics") 
    mylab3 = Label(labelWindow, text=" ") 
    mylab4 = Label(labelWindow, text="Just as simiple as that!") 

    #mylab.pack() #Shoving onto screen, automatic resize
    mylab1.grid(column=0, row=0) #grid, no automatic resize
    mylab2.grid(column=0, row=0)
    mylab3.grid(column=0, row=2)
    mylab4.grid(column=0, row=3)

def buttonwin():
    buttonWindow = Toplevel()
    buttonWindow.geometry("600x600")
    buttonWindow.title("Button's Window")
    #Creating a Button-----------------------------------------------------
    mybut1 = Button(buttonWindow, text="Click This")
    mybut2 = Button(buttonWindow, text="Disabled Button", state=DISABLED)
    mybut3 = Button(buttonWindow, text="Weird sized button", padx=40, pady=30)

    mybut1.grid(column=0, row=1)
    mybut2.grid(column=0, row=2)
    mybut3.grid(column=0, row=3)

    #Button Action
    # You can skip the mybut.grid(x,y) and instead just put the .grid(x,y) at the end of the command
    def actClick():
        mylab4 = Label(buttonWindow, text="I clicked the Action Button").grid(column=1, row=5)
    mybut4 = Button(buttonWindow, text="Action Button", command=actClick).grid(column=1, row=4)

    #colored Button
    mybut5 = Button(buttonWindow, text="Colored Font Button", fg="orange")
    mybut5.grid(column=1, row=6)

    mybut6 = Button(buttonWindow, text="Colored Box Button", bg="purple")
    mybut6.grid(column=1, row=7)
    #button 9 and 10 are taken in Entry 

def entrywin():
    entryWindow = Toplevel()
    entryWindow.geometry("600x600")
    entryWindow.title("Entry's Window")
    #Creating an Entry-----------------------------------------------------
    ent1 = Entry(entryWindow, width=50,bg="green", borderwidth=5)
    ent1.grid(column=1, row=1)

    ent2 = Entry(entryWindow)
    ent2.grid(column=1, row=2) #Entered Entry

    #Entry Get Example-----
    def entryClick(): #Action
        mylab10 = Label(entryWindow, text=ent2.get() + " : Was Entered").grid(column=1, row=4)
    mybut9 = Button(entryWindow, text="Enter Age", command=entryClick).grid(column=1, row=3)

    #Entry Insert Example----
    ent2.insert(0, "Enter the Age: ")

def Checkwin():
    CheckbWindow = Toplevel()
    CheckbWindow.geometry("600x600")
    CheckbWindow.title("Check Box's Window")
    #Creating a Check box------------------------------------ 
    def isChecked():
        mylabel = Label(CheckbWindow, text=var.get() + var2.get() ).grid(column=1, row=4)
    
    var = IntVar()
    var2 = IntVar()
    c1 = Checkbutton(CheckbWindow, text="Check Box 1", variable=var).grid(column=1, row=1)
    c2 = Checkbutton(CheckbWindow, text="Check Box 2", variable=var2).grid(column=1, row=2)

    mybutt = Button(CheckbWindow, text="Selected", command=isChecked).grid(column=1, row=3)

def radiowin():
    radioWindow = Toplevel()
    radioWindow.geometry("600x600")
    radioWindow.title("Radio Button's Window")
    #Creating a Radio Button--------------------------------- 
    def radioClick():
        select1 = Label(radioWindow, text="YOU SELECTED: " + str(radioVar.get())).grid(column=1, row=0)
    
    radioVar = IntVar()
    rb1 = Radiobutton(radioWindow, text="Radio Button 1", value=1, variable=radioVar, command=radioClick ).grid(column=1, row=1)
    rb2 = Radiobutton(radioWindow, text="Radio Button 2", value=2, variable=radioVar, command=radioClick ).grid(column=1, row=2)
    
def dropbwin():
    dropboxWindow = Toplevel()
    dropboxWindow.geometry("600x600")
    dropboxWindow.title("Drop-Down Box's Window")
    #Creating a Drop down box-------------------------------- 
    dropClick = StringVar()
    dropClick.set("A")
    dropbox = OptionMenu(dropboxWindow, dropClick, "A", "B", "C"). grid(column=1, row=1)

    
#MAIN-------------------------------------------
# This needs to be at the bottom since py reads defs first
root = Tk() #before anything else
root.title("Python GUI Introduction")
root.geometry("330x110")
root.grid()

space0 = Label(root, text="          ").grid(column=0, row=1)
space1 = Label(root, text="          ").grid(column=0, row=2)
LabelButt = Button(root, text="Labels", command=labelWin).grid(column=1, row=1)
ButtButt = Button(root, text="Buttons", command=buttonwin).grid(column=2, row=1)
EntryButt = Button(root, text="Entry", command=entrywin).grid(column=3, row=1)
CheckbButt = Button(root, text="Check box", command=Checkwin).grid(column=1, row=2)
RadioButt = Button(root, text="Radio Button", command=radiowin).grid(column=2, row=2)
DropdButt = Button(root, text="Drop-Down Box", command=dropbwin).grid(column=3, row=2)



space2 = Label(root, text="").grid(column=4, row=10)
Xexit = Button(root, text="Quit", command=root.quit).grid(column=4, row=11)
root.mainloop()