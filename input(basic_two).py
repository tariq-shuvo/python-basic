# exception handling in python
try:
    x = input("Please enter your name\n")
    print(x)
except:
    print("something going wrong")
finally:
    print("this is final statement")

# to check exception if user input string
try:
    birth_year = int(input("Please enter your birth year!\n"))
    print(birth_year)
except ValueError:
    print("This is not a valid number")