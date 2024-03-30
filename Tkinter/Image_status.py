#Imports
from tkinter import *
from PIL import ImageTk, Image

#Calls on global show images, previous button and next button
#from there we ask the grid to forget the image and load up the prev image
#Re-call the next and prev button along with the status. With next imageNum+1, prev imageNum-1
def backwards(imageNum):
    global showImage, prevButton, nextButton
    
    showImage.grid_forget()
    showImage = Label(image=imageList[imageNum-1])
    showImage.grid(row=0, column=0, columnspan=3) 
    
    nextButton = Button(root, text=">>", command=lambda: forwards(imageNum+1))
    nextButton.grid(row=1, column=2)   
    
    prevButton = Button(root, text="<<", command=lambda: backwards(imageNum-1))
    prevButton.grid(row=1, column=0)
    
    #min 1 images and then disabled prev button
    if imageNum == 1:
        prevButton = Button(root, text="<<", state=DISABLED)
        prevButton.grid(row=1, column=0)
        
    status = Label(root, text="image " + str(imageNum) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(column=0, row=2, columnspan=3, sticky=W+E,) 

#Calls on global show images, previous button and next button
#from there we ask the grid to forget the image and load up the next image
#Re-call the next and prev button along with the status. With next imageNum+1, prev imageNum-1
def forwards(imageNum):
    global showImage, prevButton, nextButton
    
    showImage.grid_forget()
    showImage = Label(image=imageList[imageNum-1])
    showImage.grid(row=0, column=0, columnspan=3) 
    
    nextButton = Button(root, text=">>", command=lambda: forwards(imageNum+1))
    nextButton.grid(row=1, column=2)   
    
    prevButton = Button(root, text="<<", command=lambda: backwards(imageNum-1))
    prevButton.grid(row=1, column=0)
    
    #max 4 images and then disabled next button
    if imageNum == 4:
        nextButton = Button(root, text=">>", state=DISABLED)
        nextButton.grid(row=1, column=2)
        
    status = Label(root, text="image " + str(imageNum) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(column=0, row=2, columnspan=3, sticky=W+E) 
    
#Main---------------------------------------------------------------------
root =  Tk()
root.title("Icons & Images")
root.geometry("600x800")
root.iconbitmap('Images/favicon.ico')

#Images 0-3, 4 in total
myImage0 = ImageTk.PhotoImage(Image.open("Images/cover0.png"))
myImage1 = ImageTk.PhotoImage(Image.open("Images/cover1.png"))
myImage2 = ImageTk.PhotoImage(Image.open("Images/cover2.png"))
myImage3 = ImageTk.PhotoImage(Image.open("Images/cover3.png"))
imageList = [myImage0, myImage1, myImage2, myImage3]

#Calls on Image to show it
showImage = Label(image=myImage0)
showImage.grid(row=0, column=0, columnspan=3)

#Previous Button, aka go back button, similar to nextButton we start at two since we will not be able to go back since no images exist past cover0, so we start at two and in prevButton we do minus 1
nextButton = Button(root, text=">>", command=lambda: forwards(2))
prevButton = Button(root, text="<<", command=lambda: backwards(2), state=DISABLED)
prevButton.grid(row=1, column=0)

#Exit the program
exitButton = Button(root, text="Exit", command=root.quit)
exitButton.grid(row=1, column=1)

#We chose the second image, because of the prevButton, we will not be able to go back since no images exist past cover0, so we start at two and in nextButton we do minus 1
nextButton = Button(root, text=">>", command=lambda: forwards(2))
nextButton.grid(row=1, column=2)

#Status of Label has, text, str(length of image List), board of 1, Sunken into the screen, anchored to the East(right) of the screen
status = Label(root, text="image 1 of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
#sticky does north to South, to East, to West, so when we say W+E caause it equals West+East
status.grid(column=0, row=2, columnspan=3, sticky=W+E,) 

root.mainloop()