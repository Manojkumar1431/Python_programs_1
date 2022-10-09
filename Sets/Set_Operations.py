number1 = {1, 2, 3, 4, 5}
number2 = {4, 5, 6, 7}
number3 = {6, 7, 8, 9}

# union operation
numbers = number1.union(number2, number3)
print(numbers)


# Intersection operation : it will find the common elements from the two sets
numbers_1 = number1.intersection(number2)
print(numbers_1)

numbers_2 = number2.intersection(number3)
print(numbers_2)


# difference operation : it will delete the common elements from the sets and print the remaining
numbers_3 = number1.difference(number2)
print(numbers_3)

numbers_4 = number2.difference(number3)
print(numbers_4)


# intersection_update() : it is used to update the number1 set directly
number1.intersection_update(number2)  # here the number1 set is updated,the number1 set will now contain elemts which are common from both the sets.
print(number1)


# difference_update() : it is also directly update the number2 set
number2.difference_update(number3)
print(number2)

# isdisjoint() operation : here if there is any common elements in both sets it will print False if not True.
{1, 2, 3}.isdisjoint({1, 5, 6})  # generally the output will be in boolean format either True or False.

# subset(), superset()