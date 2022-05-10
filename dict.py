# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "green", "blue"]
}

for x in thisdict:
  print(thisdict[x])
  
for x in thisdict.values():
  print(x)
  
for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

print(thisdict)
print(len(thisdict))
print(thisdict.get("colors"))
print(thisdict.keys())
print(thisdict.values())

thisdict["year"] = 1977

print(thisdict)

if "model" in thisdict:
    print("yes")
    
thisdict.update({"brand": "BMW"})
print(thisdict)

del thisdict["year"]
print(thisdict)

thisdict.pop("model")
print(thisdict)