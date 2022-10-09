class Dog:

    __species = 'Husky'

    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed
        self.__tricks = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

s1 = Dog('chimpu', 'Lab' )
