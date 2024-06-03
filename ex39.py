# mapping of states to their abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# states and cities in it
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])


print('-' * 10)
# Print the states using keys
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])


print('-' * 10)
# Print the cities from dict using keys
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


print('-' * 10)
# The loop prints each state name along with its abbreviation.
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


print('-' * 10)
# same for cities
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")


print('-' * 10)
# Iterate through the states dictionary and print each state with its abbreviation and corresponding city
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print('-' * 10)
# Try to get the abbreviation for Texas
state = states.get('Texas')

# Check if Texas is in the states 
if not state:
    print("Sorry, no Texas.")

# Tchecking for TX in cities , if not found default msg to store
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")