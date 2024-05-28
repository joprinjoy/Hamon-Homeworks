#function takes multiple arguments to the tuple args
def print_two(*args):
    #unpacking the arguments
    arg1 ,arg2 = args
    print(arg1)
    print(arg2)

#function takes  two arguments
def print_two_again(arg1,arg2):
    print(f"arg1:{arg1} and arg2: {arg2}")

#function takes one argument
def print_one(arg1):
    print(f"I have only one argument:{arg1}")

#function without arguments
def print_none():
    print("I got nothing")

#function call with multiple parameteres
print_two("Joprin","Joy")
#function call with two parameteres
print_two_again("Joprin","Joy")
#function call with one parameters
print_one("joprin")
#function call without parameters
print_none()