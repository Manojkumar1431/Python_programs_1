Example = [1, 2, 3, 4, 5, 6]

# slicing syntax [starting index no : Ending index no] remember index counting starting from 0 onwards
slice1 = Example[0:3]
print(slice1)


# retrieving elements from backward
slice2 = Example[-4:-1]
print(slice2)

slice3 = Example[2:-2]  # here -2 used to count index number from backward
print(slice3)



# step size
slice4 = Example[0:5:2]
print(slice4)

slice5 = Example[1:-1:3]
print(slice5)


# prints elements in reverse order
slice6 = Example[::-1]
print(slice6)



