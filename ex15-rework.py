from sys import argv

script, filename = argv

#create a new variable called txt, which will run the open(filename) command.
txt = open(filename)

print(f"Here's your {filename}:")
#notice that you could remove line 6 and then replace txt with open(filename)
print(txt.read())

print("Type the filename again:")
file_again = input(">>> ")

txt_again = open(file_again)

print(txt_again.read())
