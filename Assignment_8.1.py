#<Justin Carter>
#<04OCT2020>
#Writing a Python program that has you interacting with the file system.
# Some supporting information taken from https://www.tutorialspoint.com/python/python_files_io.htm

import os

#Prompt the user for the name of the directory
fileLocation = input("Please enter the file path:")

#Prompt the user for the name of the file
fileTitle = input("Please enter the file name:")

#if the directory doesn't exist the program must create the specified directory
if not os.path.exists(fileLocation):
    os.makedirs(fileLocation)
entireEntry = os.path.join(fileLocation, fileTitle + ".txt")


#Prompt the user for their name, address, and phone number 
fileData = open(entireEntry, "w")
userName = input("Please enter a name:")
userAddress = input("Please enter an address:")
userPhone = input("Please enter a phone number:")

#write that data as a line of comma separated values to the file
fileData.write(userName+', '+userAddress+', '+userPhone+'\n')
fileData.close()

#After the data has been written to the file your program must open the file, read the contents, and display the contents to the user as program output.
fileData = open(entireEntry, "r")
print(fileData.read())
