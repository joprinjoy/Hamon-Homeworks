#variable
types_of_people = 10

#another variable with formating to include value of another variable

x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

#variable  takes  string with formating and includes values of two variables
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)


print(f"I said: {x}")

print(f"I also said: '{y}'")

#variable with boolean value
hilarious = False

#variable  with a string and empty curly brackets to recieve the formating values later

joke_evaluation = "Isn't that joke so funny?! {}"

#sending value of hilarious to the formating in joke_evaluation

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

#adding two strings and printing
print(w + e)