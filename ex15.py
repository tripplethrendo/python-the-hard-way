from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file: \n***{filename}***")
print(txt.read())

print("Type the filename again:")
file_again = input("λ ")

txt_again = open(file_again)

print(txt_again.read())
