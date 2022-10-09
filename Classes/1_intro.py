class Student:
    pass

obj1 = Student()

obj2 = {}

print(obj1)

print(isinstance(obj1, Student))  # to know whether the obj1 is instance of class or not if yes (True) else False

print(isinstance(obj2, Student))  # here the result is False because obj2 is not instance of class Student

#  adding attributes to class/objects
class Student1:
    name = ''
    role = 'ASE'
    active = True

s1 = Student1()
s1.name = 'Manoj'
s1.active = False

print(s1.name, s1.role, s1.active)


