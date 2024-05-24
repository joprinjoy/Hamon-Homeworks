from sys import argv

# importing exists to perform compare
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

#storing the file to in_file
in_file = open(from_file)

# reading the contents of the file and storing to indata
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")


#checking whether to_file is existing in the directory or not
print(f"Does the output file exist{exists(to_file)}")

print(f"Ready ,hit return button to continue, CTRL-C to abort. ")
input()

#opening the file in write mode and writing the content
out_file = open(to_file,'w')
out_file.write(indata)

print("Alright,all done.")

#closing all opened files
out_file.close()
in_file.close()