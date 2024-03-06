#General open methods to use open a text file
#You must uncomment one section to run

#Section 1
f = open("Python-Basics\File\TextFile.txt", "r")         #Open File

#Prints all in Text file-------------------------------------------
#print(f.read())                                         #Remove '#' to see how it works


#Prints only first 6 letters-------------------------------------------
#print(f.read(6))                                        #Remove '#' to see how it works


#Prints only first 6 letters-------------------------------------------
#print(f.readline())                                     #Remove '#' to see how it works


#Section 2
#Writes-------------------------------------------
# f = open("Python-Basics\File\TextFile.txt", "a")        #Open File, 'a' - append
# f.write("This will add more data to the file!")         #Write data into the file
# f.close()                                               #Close file

# f = open("Python-Basics\File\TextFile.txt", "r")        #Open File, 'r' - read
# print(f.read())                                         #Reads file


#Section 3
#Create a new file---------------------------------------------
file = open("Python-Basics\File\MyFile.txt", "x")       #Open File, 'x' - create
file.close()                                            #Close file

#Delete a file-----------------------------------------
import os
if os.path.exists("Python-Basics\File\MyFile.txt"):     #Checks to see if file exist
    os.remove("Python-Basics\File\MyFile.txt")          #Deletes the file if exist
else:
    print("MyFile.txt is Gone")                         #File does not exist

