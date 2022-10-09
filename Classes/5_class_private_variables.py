class Dog:
    def __init__(self, name, breed):
        self.__name = name  # declaring attributes with private
        self.__breed = breed

    def print_details(self):
        return "Hello people I'm %s and i am a %s breed" % (self.__name, self.__breed)

s1 = Dog('Tommy', 'lab')
print(s1.print_details())

# trying to update __name but it wont be updated because it was in private, so we cant update it outside of a class
s1.__name = 'Scissor'
print(s1.print_details())

"""
we can update attributes by placing single dash in front of "_class name" and double dash infront of attribute 
name (__name) 
"""
s1._Dog__name = 'stanze'
print(s1.print_details())



