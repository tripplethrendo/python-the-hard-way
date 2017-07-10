#load the argv module
from sys import argv

#give the argv command some inputs
script, filename = argv

#use the open command on our filename
txt = open(filename)

#print the filename of the input
print(f"Here's your file: \n***{filename}***")
#print out the text of the file
print(txt.read())

#tell the user to  input a file name again
print("Type the filename again:")
#create a variable called file_again, then create an input with a special symbol
file_again = input("λ ")

#the variable txt_again will now run the variable file_again
txt_again = open(file_again)

#print out the stored variable we received from file_again
cuprint(txt_again.read())
