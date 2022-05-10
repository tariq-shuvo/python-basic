# A tuple is a collection which is ordered and unchangeable.
myTuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
print(myTuple[0])
print(myTuple[-1])
x = list(myTuple)
x[1] = "kiwi"
myTuple = tuple(x)
print(myTuple)

# unpack
(green, yellow, *red) = myTuple
print(green)
print(yellow)
print(red)