class Student:
    dept = 'CSE'  # created a class variable
    Student_data = []  # created empty list

    def __init__(self, name, Id):
        self.name = name
        self.Id = Id
        self.email = name+'@gmail.com'

    def regnum(self):
        return self.name, self.Id

    def display(self):
        return 'name : ', self.name, 'Id : ', self.Id, ' Dept : ', self.dept

s1 = Student('Mintu', 123)
s1.dept = 'MECH'  # updating dept value with instance self so, it will be updated only for s1 object not entire class
print(Student.dept)

print(s1.display())

Student.Student_data.append(s1.display())  # appending data into empty list
print('List ', Student.Student_data)

Student.dept = 'IT'  # updating the dept value with class name so, it will be updated entirely

print(s1.display())

s2 = Student('Manoj', 345)
print(s2.display())





