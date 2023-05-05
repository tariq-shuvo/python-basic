import json

x = '{ "name":"John", "age":30, "city":"New York"}'

# string to json convert
y = json.loads(x)

print(y)

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into json
# json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)
y = json.dumps(x)

print(y)

