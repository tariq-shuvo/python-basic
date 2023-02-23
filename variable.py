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
# complex_value.real (10) complex_vlue.imag (1j) 
complex_value = 10 + 1j # real(10) + imagenary(1j)

# list of data which is changeble and traversed by index number
list_value = ["apple", "banana", "cherry", "apple"]

# list of data which can't be changed just can be added new data into the tuple
tuple_value = ("apple", "bannana", "cherry", "apple")

# list of data which avoid repeatation able to do union, intersection, differance, add, update, remove, discard
set_value = {"apple", "bannana", "cherry", "apple"}

# list of data represent as set but its immutable
frozen_set_value = frozenset({"apple", "bannana", "cherry", "apple"})

range_value = range(6) # range(start, end, interval) this will create a list
dict_value = {"name": "jhon", "age": 25}
bool_value = True

# byte value range must be 0 to 255 value can't be modified(immutable)
byte_value = b"Hello"
# byte array value range must be 0 to 255 value can be modified(mutable)
byte_array_value = bytearray(5)
# get memory value of byte value which can be directly visited value using memory view like memoryview_value.obj which will be effective for high performance  
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
