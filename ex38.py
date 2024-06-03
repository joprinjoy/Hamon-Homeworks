# string stored in variable
ten_things = "Apples oranges crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# converting the string into list of different words using split
stuff = ten_things.split(' ')  

#another list containing stuffs to append into 10 things
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# want to make the list of 10 items
while len(stuff) != 10:
    # assigning fuction to remove the last item from more stuff list and storing to a variable, next time variable name will be using for the last popped item
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # Appending the removed item to stuff
    stuff.append(next_one)
    # Printing number of items in stuff
    print(f"There are {len(stuff)} items now.")

#after the list having 10 items
print("There we go: ", stuff)

print("Let's do some things with stuff.")

# Printing the second item in the list (index 1)
print(stuff[1])

# Printing the last item in the list
print(stuff[-1])

# Remove and print the last item in the list
print(stuff.pop())

# Join the items in the list with a space and print the resulting string
print(' '.join(stuff))

# Join the the items in range of 3-5
print('#'.join(stuff[3:5]))