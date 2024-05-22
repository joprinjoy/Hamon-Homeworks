#variable with four recievers
formatter = "{} {} {} {}"

#passing 4 int values
print(formatter.format(1,2,3,4))

#passing 4 string values
print(formatter.format('one','two','three','four'))

#passing 4 boolean values
print(formatter.format(True,False,True,False))

#passing the same reciever variable
print(formatter.format(formatter,formatter,formatter,formatter))

print(formatter.format("Twinkle Twinkle Little star\n","how i wonder what you are\n","up above the world so high\n","like a diamond in the sky"))   