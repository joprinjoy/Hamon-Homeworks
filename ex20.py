from sys import argv
script, input_file = argv
#function to print whole file
def print_all(f):
    print(f.read())
#seting the byte to zero to start reading the file again
def rewind(f):
    f.seek(0)
#fuction to read line.files are read line by line so no need to mention the index
def print_a_line(line_count,f):
    print(line_count,f.readline())
#open the file to this variable
current_file = open(input_file)
#function call print_all with the open file as parameter
print("Lets print the whole file")
print_all(current_file)

#function call for rewind
print("Now lets rewind,Kind of like a tape")
rewind(current_file)

#setting a variable to disply the line number along with lines
current_line=1
#function call with open file and line  number as parameter
print_a_line(current_line,current_file)

current_line=current_line + 1
print_a_line(current_line,current_file)

current_line=current_line + 2
print_a_line(current_line,current_file)
