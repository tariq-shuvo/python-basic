# A tuple is a collection which is ordered and unchangeable. Its allowed duplicates.
"""
list.append('item value') to add items into the tuple by costing tuple as list the append into list
tuple_list += another_tuple_list to merge two tuple list items
tuple_list.count(item_value) to count the number of values inside the list
len Used to find out the length of an tuple
"""
myTuple = ("apple", "banana", "cherry", "strawberry", "raspberry", "apple")
print(myTuple.count('apple'))
print(myTuple.index('cherry'))
print(len(myTuple))
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