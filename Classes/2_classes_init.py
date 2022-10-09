"""
when we declare any functions inside a class those are called "methods"
"""

class School:
    # here __init__ is a special method, the argument (self) is used to automatically invoke the __init__ method
    def __init__(self):
        print("Welcome to class, initialized successfully")

obj1 = School()

# ==================Methods with arguments============================================================
class Library:
    def __init__(self, name):
        self.name = name
        self.author = name+' published by Mintu'

obj2 = Library('Atomic science')

print(obj2.name, obj2.author)

# ===================adding more methods=======================================================

class Student:
    def __init__(self, last, first):
        self.last = last
        self.first = first
        self.mail = first, last+"@gmail.com"

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def uppercase(self):
        self.first = self.first.upper()
        self.last = self.last.upper()

s1 = Student('B', 'Manoj')

print(s1.full_name())

s1.uppercase()  # by calling the method here it is converted to uppercase as per the functionality

print(s1.full_name())

