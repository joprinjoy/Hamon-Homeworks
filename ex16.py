from sys import argv

script, filename = argv

#printing informational msges to user
print(f"We are going to erase {filename}")
print("If you don't want that, hit CTRL-C.")
print("If you want that , hit Return.")

#waiting for an input
input("?")

#opening the file

print("Opening the file..")
target = open(filename,'w')

#emtying the file 

print("Truncating the file.Goodbye!")
target.truncate()

print("Now I am going to ask you to write three lines.")

#taking lines from user
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line3 : ")

print("I'm going to write these lines to the file.")

#Writing lines to the file
target.write(line1)
#\n set the next line
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

#closing the file
print("Finally, we close it")
target.close()


