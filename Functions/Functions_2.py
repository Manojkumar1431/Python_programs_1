# keyword arguments function

def keyword_arg_fun(maths, physics, chemistry, social):
    print("My scores in each subject is,\nin maths :", maths, "\nphysics ", physics, "\nchemistry : ", chemistry, "\n social : ", social)
    return "total score is : ", maths+physics+chemistry+social

# we are mentioning keyword arguments so that there is no confusion while assigning values to the arguments
score = keyword_arg_fun(maths=30, physics=40, chemistry=56, social=34)
print(score)
print("\n")


# ===================================================================================================================
# using *args to mention many arguments without specifying

def fun1(*args):  # here we can input any number of values while calling function, the output is in tuple format
    print(args)

fun1('apple', 'banana', 'carrot', 'doughnut')
print("\n")


def students(college, city, *Students):
    print("College : ", college)
    print("City : ", city)
    print("Students name : ", Students)

students('GuruNanak', 'HYD')
print("\n")

students("GNI", 'Hyderabad', 'Manoj', "mintu", "Nikhil")
print("\n")

# it will throw an error because when we mention value to a keyword argument some pattern should be followed "positional arguments followed by keyword argument"
""" students("MGIT", city="WGL", 'Mango','banana') """


def students_1(*Students1, college, city):
    print("College : ", college)
    print("City : ", city)
    print("Students name : ", Students1)

students_1('apple', 'banana', college='MGITL', city="WGL")

# ======================================================================================================================
# built-in functions with keyword arguments

num_list = [5, 3, 6, 9, 1]
a = sorted(num_list)
print(a, "\n")

# here we are mentioned an in built keyword argument reverse=True which reverse the list
b = sorted(num_list, reverse=True)
print(b)
print("\n")

# using "sep" builtin keyword
print("Manoj", "Mintu", "Nikhil", sep="|")
print("\n")

# using "end" keyword
print("Manoj", "Mintu", "Nikhil", sep="|", end="********")
print("\n")