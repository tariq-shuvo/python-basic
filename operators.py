x = 10
y = 15
z = x
# Arithmetic operators 
print(x + y)   # add
print(y - x)   # substruct 
print(x * y)   # multiply
print( x / y)  # division
print( x // y) # floor division 
print( x % y)  # Modulus
print( x ** y) # power x of y

# Comparison operators 
print(x == y)   
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)
print(x != y)

# Logical operators 
print(x >= 10 and y >= 15)
print(x >= 10 or y <= 15)
print(not(x >= 10 or y <= 15))

# Identity Operators
print(x is z)
print(x is y)

# Membership Operators
list1 = ["apple", "banana"]
data1 = "apple"

print(data1 in list1)
print(data1 not in list1)

# what is the difference between == and is operator. Ans. is operatior is work on based on variable and == operator work on value
a = [10, 20, 22, 25]
b = a
c = a[:]
print("b is a", b is a) # True
print("c is a", c is a) # False
print("c = a", c == a) # True