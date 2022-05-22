# Python program to open a text file

import time                                     #for time.sleep to read one at a time

#Opens a text file
with open("Python-Basics\File\TextFile.txt", "r") as txtfile: #Open
    fileopen = txtfile.read().splitlines()      #Reads the information
    
    #Prints out lines in the text file
    for line in fileopen:                       
        print(line)
    #time.sleep(1)                              #reads line one at a time

txtfile.close()                                 #Closes Text File


print("\n")
#CSV File------------------------------------------------------------
#Import csv mod
import csv

#opens CSV File
with open('Python-Basics\File\CVSFile.csv','r') as csvfile:   #Open
    csvOpen = csv.reader(csvfile)               #Reads the information
    #next(csvOpen)                              #Skips first line            
    
    #Prints out items in the Csv file
    for items in csvOpen:
        print(items)
    
csvfile.close()                                 #Close CSV File