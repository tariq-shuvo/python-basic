# List in python
# List is a collection which is ordered and changeable. Allows duplicate members.

myList = ["apple", "banana", "cherry"]

# for loop
for x in myList:
    print(x)
    
for i in range(len(myList)):
    print(i)    

# while loop
i = 0
while i < len(myList):
    print(i)
    i = i + 1 
    
# list comprehension
newList = [x for x in myList if "a" in x]
print(newList)
     
print(myList)
print(myList[0]) #accessing data
print(myList[-1]) #accessing data
print(myList[1:]) #accessing data

if "apple" in myList:
    print("Yes, apple is in the fruit list")
    
anotherList = list(("plam", "grap", "berry", "berry"))
print(anotherList)
anotherList[1:3] = ["watermalon"]
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

"""
myList.clear()
myList.append("orange")
print(myList)
print(anotherList.count("berry"))
x = myList.copy()
print(x)
myList.extend(anotherList)
print(myList)
print(myList.index("berry"))
myList.insert(len(myList), "cherry")
print(myList)
anotherList.pop()
print(anotherList)
anotherList.remove("plam")
print(anotherList)
myList.reverse()
print(myList)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True) # reverse Optional. reverse=True will sort the list descending. Default is reverse=False

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

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

print(cars)
print(len(cars))