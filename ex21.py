#function to add two numbers passed as arguments and retrun its result
def add(a,b):
    print(f"ADDING {a} + {b} ")
    return a+b

def subtract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiply {a} x {b}")
    return a* b

def divide(a, b):
    print(f"Divide {a} / {b}")
    return (a/b)

#calling a function is assigned to variable so that everytime the variable is printing the function is called
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"age:{age} height:{height} Weight :{weight} Iq : {iq}")

print("here is the puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("THat becomes: ",what,"can you do it by hand")

