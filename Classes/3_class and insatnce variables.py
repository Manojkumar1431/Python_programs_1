class Competition:
    raise_amount = 1.5  # class variable

    def __init__(self, price, amount):
        self.price = price
        self.amount = amount

    def raise_excepted(self):
        # calling class variable by mentioning class name
        # self.amount = self.amount * Competition.raise_amount
        """ We can also call class variable by self keyword,
         when we update class variable value by self then it will be updated there itself not entirely """
        self.amount = self.amount * self.raise_amount


s1 = Competition('Bike', 500)

print(s1.price, s1.amount)

s1.raise_excepted()
print(s1.amount)

s1.raise_excepted()
print(s1.amount)

print("\n")

s2 = Competition('Car', 200)

print(s2.price, s2.amount)
s2.raise_amount = 30
s2.raise_excepted()
print(s2.amount)

# NOTE
''' calling class variable with self keyword difference between calling class variable by class name 
and self when we update the class variable value by class name then it will get updated everywhere 
where as when we update class variable value by self then it will be updated there itself not entirely
'''
