def my_introduction():
    print("Welcome to Functions Module")
    print("My name is Manojkumar")
    print("I am a Data Analyst")

my_introduction()  # calling the function by just calling with the function name
print(end="\n")


# ==========================================================================================================
# Documented function means comments

def documented_func():
    """This is a documented function"""
    print("Hello World")

print(documented_func.__doc__)
# if we type functionname.__doc__ it will show us all the documented text from that function

new_documented_func = documented_func  # copying the function to a variable
new_documented_func()  # calling the new copied function with paranthesis
print("\n")
# ===============================================================================================================
# function with parameters
def my_fun(name, age):
    print("Hello, My Name is ", name)
    print("My age is ", age)

my_fun('Manoj', 22)
print("\n")

''''# user input to the arguments name and age
name1 = str(input("Enter name: "))
age1 = int(input("enter age: "))
my_fun(name1, age1)
'''
print("\n")


# ====================================================================================================================
# function with "return" values

def fun_return(num1, num2):
    return num1+num2

b = fun_return(10, 20)
print(b)

# function with many return values
def fun_return1(number1, number2):
    add = number1 + number2
    sub = number1 - number2
    return add, sub

c = fun_return1(50, 20)
print(c)

# assigning 2 return values to two variables individually to call them separately
result_1, result_2 = fun_return1(40, 20)
print(result_1)  # return add is assigned to result_1
print(result_2)  # return sub is assigned to result_2

# if we want to ignore any return value just mention "_" in that place
result_3, _ = fun_return1(30, 20)
print(result_3)
print("\n")

# ===============================================================================================================
# Dictionary inside a function
def dict_func(name, age, occupation):
    dict1 = {
        'Name': name,
        "Age": age,
        'occupation': occupation
    }
    return dict1

output = dict_func('Mintu', 34, 'software designer')
print(output)