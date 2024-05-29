#run program as python3 ex23.py utf-8 strict where, utf8-encoding and strict - error handle method
import sys
#unpacking the argv (argument variable)
script, encoding, error = sys.argv

#main function ,read the line and call another function for encoding
def main(language_file, encoding, errors):
    
    #Reading the first line to be read, if line present then calls another function called print_line
    #Returning to main function to complete other lines
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
#nested function definition , takes line ,encoding ,error handle as arguments to 
def print_line(line, encoding, errors):
    #storing the line after striping the leading and tailing whitespaces
    next_lang = line.strip()
    
    #encoding the line and storing to variable
    raw_bytes = next_lang.encode(encoding, errors = errors)

    #decoding the encoded line and storing to variable
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)

#opening the targeted file with encoding 
languages = open("languages.txt", encoding ="utf-8")

#calling main function with opened file encoding and error as parameters
main(languages, encoding, error)