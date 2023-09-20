# string manipulation
course = "python for beginners"
print(course[0])
print(course[1])
print(course[-1])
print(course[-2])
print(course[1:5]) # from 1 index to 5 (excluding 5)

# string with dynamic variable
name = "muhammad"
message = f"Hi, Our prophet name is {name}"
print(message)

price = 49
txt = "The price is {} dollars"
txt_fraction = "The price is {:.2f} dollars"
print(txt.format(price))
print(txt_fraction.format(price))

# use multple variable in string formating need maintain serial
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# multiple parameter in string formating no serail needed
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(model = "Mustang", carname = "Ford"))

# string related functions
print(message.upper())
print(message.lower())
print(message.title())
print(message.find('Our'))
print(message.replace('Our', 'My'))
print("Our" in message)
print(message.capitalize())