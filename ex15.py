from sys import argv

script, filename = argv

#opening file and storing to txt

txt = open(filename)


#reading the file by variablename.read()

print(f"Here is your file {filename} :\n")
print(txt.read())

#another way of opening file within the code

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())