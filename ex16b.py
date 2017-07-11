from sys import argv

script, filename = argv
with open(filename) as f:
    output = f.read()

print(f"We're going to erase {filename}.")
print("If you don't want to erase the file, hit CTRL-C (^C).")
print("If you do want to erase the file, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

#print the filename of the input
print(f"Here's your file: \n***{filename}***")
#print out the text of the file
txt = open(filename)
print(txt.read())

print("And finally, we close it.")
target.close()
