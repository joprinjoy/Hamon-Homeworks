#declaring  variable cars and assigning value

cars=100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers

#multiplying/dividing the values of two variables and storing it to another one

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#printing the value of variable inbetween the strings

print("There are",cars,"cars available")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport ",carpool_capacity,"peoples today")
print("We have ",passengers,"to carpool today")
print("We need to put about",average_passengers_per_car,"in each car")



