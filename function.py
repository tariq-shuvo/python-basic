# A function is a block of code which only runs when it is called.
from unittest import result


def my_function(name):
    print("Hello "+ name)

my_function("Bangladesh")

def tuple_args(*name):
    print(name)
    
tuple_args("Bangladesh", "Bhutan", "Nepal")


def dict_args(**dict_value):
    print(dict_value)
    
dict_args(country="Bhutan", name="Anis", age=25)

def tri_recursion(n):
    if(n > 0):
        result = n + tri_recursion(n-1)
        print(result)
    else:
        result = 0  
        print(result)
    return result

print("Tri recursion result is:")
tri_recursion(6)  

x = lambda a, b: a + b

print("Lamda Func: " + str(x(10, 5)))