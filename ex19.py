#frunction with two arguments
def cheese_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man thats's enough for the party")

#function call with two parameters
print("We can just give the function numbers directly:")
cheese_crackers(20, 30)

print("OR,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#functoin call with two variables as parameters
cheese_crackers(amount_of_cheese,amount_of_crackers)

#function call with result of  two math operations as parameters
print("we can even do math inside too:")
cheese_crackers(10+20,5+6)
