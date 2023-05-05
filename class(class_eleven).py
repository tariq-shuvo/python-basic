class MyClass:
    x = 5
    
p1 = MyClass()
print(p1.x)
# parernt class
class Person:
    def __init__(self, name, age, designation, country):
        self._name = name
        self.age = age
        self.designation = designation
        self.country = country
        
    def getName(self):
        return self._name
        
person1 = Person("Anis", 25, "Executive", "AUS")
print(person1.getName())
print(person1.age)
print(person1.designation)
print(person1.country)

#child class
class Student(Person):
    def __init__(self, name, age, designation, country, section):
        super().__init__(name, age, designation, country)
        self.section = section

student1 = Student("kamal", 15, "Class 9", "BD", "A")
print(student1.getName())
print(student1.section)