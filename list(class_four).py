# List in python
# List is a collection which is ordered and changeable. Allows duplicate members.

myList = ["apple", "banana", "cherry"]
print(myList, "list elements are shown. Start For Loop ...")

# for loop
for x in myList:
    print(x)

print("For loop has been completed. Start For Loop with range list ...")

for i in range(len(myList)):
    print(f"{i} = {myList[i]}")  

print("For loop with range array has been completed. Start For Loop with range (start, end, interval) list ...")

# create range list and print out
for j in range(10, 20, 2):
    print(j)  

print("For loop with range(start, end, interval) array has been completed. Start while loop with list")

# while loop
i = 0
while i < len(myList):
    print('index', i, 'value is ', myList[i])
    i = i + 1 

print("While loop has been completed.")    

# list comprehension to make custom iteration [output expression, input sequence, conditional logic]
newList = [x for x in myList if "a" in x]
print(f"list comprehension {newList}")

# even square list using comprehension
newEvenSquareList = [i**2 for i in range(20) if i % 2 == 0]
print(newEvenSquareList)

print(myList)
print(myList[0]) #accessing data
print(myList[-1]) #accessing data
print(myList[1:]) #accessing data

if "apple" in myList:
    print("Yes, apple is in the fruit list")
    
anotherList = list(("plam", "grap", "berry", "berry"))
print(anotherList)
anotherList[1:3] = ["watermalon"] # replacing value of array
print(anotherList)

# List Methods
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
del array[index] Use to delete element from list
len Used to find out the length of an array
"""
myList.clear()
print(f"clear() {myList}")
myList.append("orange")
print(f"append() {myList}")
print(f"count() {anotherList.count('berry')}")
x = myList.copy()
print(f"copy() {x}")
myList.extend(anotherList)
print(f"extend() myList with anotherList {myList}")
print(f"index() {myList.index('berry')}")
myList.insert(len(myList), "cherry")
print(f"inset() {myList}")
anotherList.pop()
print(f"pop() {anotherList}")
anotherList.remove("plam")
print(f"remove() {anotherList}")
myList.reverse()
print(f"reverse() {myList}")

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True) # reverse Optional. reverse=True will sort the list descending. Default is reverse=False
print(f"sort() {cars}")

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(f"as key function apply in sort() {cars}")

# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(reverse=True, key=myFunc)

print(f"Reverse True and as key function apply in sort() {cars}")