# variable declaration process 
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

x = 5 #int 
y = "Jhon" #str
z =  True #bool
k = float(5) #casting

print(x)
print(y)
print(z)
print(k)

# type checking
print(type(x))
print(type(y))
print(type(z))
print(type(k))

str_message = "Hello Bangladesh"
int_value = 20
float_value = 20.5
complex_value = 1j
list_value = ["apple", "banana", "cherry", "apple"]
tuple_value = ("apple", "bannana", "cherry", "apple")
set_value = {"apple", "bannana", "cherry", "apple"}
frozen_set_value = frozenset({"apple", "bannana", "cherry", "apple"})
range_value = range(6)
dict_value = {"name": "jhon", "age": 25}
bool_value = True
byte_value = b"Hello"
byte_array_value = bytearray(5)
memoryview_value = memoryview(bytes(5))
none_value = None
multi_line_str = """
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""
print(multi_line_str)
print(type(str_message))
print(type(int_value))
print(type(float_value))
print(type(complex_value))
print(type(list_value))
print(type(tuple_value))
print(type(set_value))
print(type(frozen_set_value))
print(type(range_value))
print(type(dict_value))
print(type(bool_value))
print(type(byte_array_value))
print(type(memoryview_value))
print(type(none_value))
