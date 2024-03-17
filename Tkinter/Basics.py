#imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root =  Tk() #before anything else
root.title("Python Tkinter Introduction")
root.geometry("700x500")

notebook = ttk.Notebook(root, width=800, height=500)
notebook.pack(pady=10)

#Created Tabs Frame 0-4
frame0 = Frame(notebook)
frame0.pack(fill='both', expand=1)
notebook.add(frame0, text='Opening Tab') 

frame1 = Frame(notebook)
frame1.pack(fill='both', expand=1)
notebook.add(frame1, text='Basic GUI Tab') 

frame2 = Frame(notebook)
frame2.pack(fill='both', expand=1)
notebook.add(frame2, text='Frame Tab') 

frame3 = Frame(notebook)
frame3.pack(fill='both', expand=1)
notebook.add(frame3, text='File Tab') 

frame4 = Frame(notebook)
frame4.pack(fill='both', expand=1)
notebook.add(frame4, text='New window Tab') 

#Frame 0 Details - Opening Details-------------------------------------------------------------------------------------------------------        
Opening = Label(frame0, text="This program goes over a series of things within the tkinter program, below is the TOC").pack(pady=10)
TableofCon = Label(frame0, text="Basic GUI Tab............Series of Labels, Buttons(radio/check box), Entry Box, Dropdown box\nFrame Tab....................................................Creates a label frame around certain GUI widgets\nFile Tab................................................................Open/Read/Write/Append/Save to a text file\nNew Window Tab............................................Opens a new window with a press of a button").pack(pady=10)


#Frame 1 Details - Labels, Buttons(radio/check box), Entry Box, Dropdown box-------------------------------------------------------------
Label(frame1, text="").grid(column=0, row=0) 
Label(frame1, text="").grid(column=0, row=1) 
Label(frame1, text="").grid(column=0, row=2) 
    #Creating a Check box------------------------------------ 
var0 = IntVar()
var1 = IntVar()
c1 = Checkbutton(frame1, text="Check Box 1", variable=var0).grid(column=0, row=3)
c2 = Checkbutton(frame1, text="Check Box 2", variable=var1).grid(column=0, row=4)
def isChecked():
    mylabel = Label(frame1, text=var0.get() + var1.get()).grid(column=0, row=6)
mybutt = Button(frame1, text="Enter >", command=isChecked).grid(column=0, row=5)

    #Creating a Radio Button--------------------------------- 
def selectin():
    select1 = Label(frame1, text="YOU SELECTED: " + str(var3.get())).grid(column=0, row=9)
var3 = IntVar()
r1 = Radiobutton(frame1, text="Radio Button 1", value=1, variable=var3, command=selectin ).grid(column=0, row=7)
r2 = Radiobutton(frame1, text="Radio Button 2", value=2, variable=var3, command=selectin ).grid(column=0, row=8)
   
    #Creating a button----------------------------------------------------
Label(frame1, text="").grid(column=1, row=0) 
Label(frame1, text="").grid(column=1, row=1) 
Label(frame1, text="").grid(column=1, row=2) 
mybut1 = Button(frame1, text="Click This").grid(column=1, row=3)
mybut2 = Button(frame1, text="Disabled Button", state=DISABLED).grid(column=1, row=4)
    #Button Action
def myClick():
    mylab3 = Label(frame1, text="I clicked the Action Button").grid(column=1, row=6)
mybut3 = Button(frame1, text="Action Button >", command=myClick).grid(column=1, row=5)

    #Colored Button Font
mybut4 = Button(frame1, text="Colored Font Button", fg="orange").grid(column=1, row=7)

    #Colored Button Box
mybut5 = Button(frame1, text="Colored Box Button", bg="purple").grid(column=1, row=8)

    #Custom button shape
Label(frame1, text="").grid(column=1, row=9) 
mybut6 = Button(frame1, text="Weird sized button", padx=50, pady=35).grid(column=1, row=10)

    #Creating an Entry-----------------------------------------------------
Label(frame1, text="").grid(column=2, row=0) 
Label(frame1, text="").grid(column=2, row=1) 
Label(frame1, text="").grid(column=2, row=2) 
ent1 = Entry(frame1, width=30, bg="green", fg="white", borderwidth=5).grid(column=2, row=3)

ent2 = Entry(frame1, width=25)
ent2.grid(column=2, row=4) #Entered Entry
ent2.insert(0, "Enter Your Age: ")

def entryAge(): #Action
    age = ent2.get().replace("Enter Your Age: ", "")
    Label(frame1, text="You are " + age + " years old.").grid(column=2, row=6)
mybut7 = Button(frame1, text="Age Entered >", command=entryAge).grid(column=2, row=5)
    
    #Creating a Drop down box--------------------------------
Label(frame1, text="").grid(column=2, row=7) 
Label(frame1, text="Drop Down Box").grid(column=2, row=8)
clicked = StringVar()
clicked.set("C")
drop = OptionMenu(frame1, clicked, "A", "B", "C"). grid(column=2, row=9)


#Frame 2 Details - Label Frame-----------------------------------------------------------------------------------------------------------
labelframe0 = LabelFrame(frame2, text="Label this Frame Here")
labelframe0.pack(padx=20, pady=20) #padding can be kept with a grid
def nextTab(): #From the blue tab(0) you you can go to the red tab(1)
    notebook.select(3)
def prevTab(): #From the red tab(1) you you can go to the blue tab(0)
    notebook.select(1)
Button(labelframe0, text="Next tab >", command=nextTab).pack(padx=20, pady=20)
Button(labelframe0, text="< Prev tab", command=prevTab).pack(padx=20, pady=20)


#Frame 3 Details - File------------------------------------------------------------------------------------------------------------------
"""
Read - r (read file)
Read and Write - r+ (beginning of file)
Write - w (over-written)
Write and Read - w+ (over written)
Append - a (end of file)
Append and Read - a+ (end of file)
"""
def openText():
    def saveText():
        fileText = open("demoFile1.txt", "w")
        fileText.write(myText.get(1.0, END))
        Label(text="Your file has been saved").pack(pady=20)
    fileText = filedialog.askopenfilename(title="open Text", filetypes=(("Text File", "*.txt"), ))
    fileText = open(fileText, "r")
    textfield = fileText.read()
    print(textfield)
    myText.insert(END, textfield)
    saveButton = Button(root, text='Save File >', command=saveText).pack(pady=20)

myText = Text(frame3, width=30, height=5, font=16)
myText.pack(pady=20)
openButton = Button(frame3, text='Open File >', command=openText).pack(pady=20)

#Frame 4 Details - New Window------------------------------------------------------------------------------------------------------------
Label(frame4, text="").pack() 
Label(frame4, text="").pack()
Label(frame4, text="").pack()
def openplz():
    top = Toplevel()
    top.title("The second window")
    label0 = Label(top, text="Thats how you opened a second window").pack()
    But1 = Button(top, text="Quit", command=top.destroy).pack()
      
butt0 = Button(frame4, text="Second window", command=openplz).pack()
root.mainloop()


#keeps GUI uploaded----------------------------------------------------------------------------------------------------------------------
root.mainloop() 