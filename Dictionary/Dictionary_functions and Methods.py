bike_info = {
    'model': 'R15V4',
    'color': 'Red',
    'year': '2022',
    'price': 206000
    }

# sorted() function used to organize the data in a ascending order( leximographical order= simply in dictionary order)
print(sorted(bike_info))

print(sorted(bike_info.keys()))
# print(sorted(bike_info.values()))  this will throw an error because in the dictionary values are of different DataTypes, where sorted function will analyse in ascending order.

# items() function it will show data in the form a tuple format
print(bike_info.items())


# copy() function
copy_bike_info = bike_info.copy()
print(copy_bike_info)

# pop() function
bike_info.pop('price')
print(bike_info)

# popitem() function, it will remove random field from the dictionary
copy_bike_info.popitem()
print(copy_bike_info)


# update() function -used to add one dictionary into another dictionary
dict_age = {"ethan": 54, "sophia": 45}
new_dict_age = {"ethan": 78, "Harper": 67}

dict_age.update(new_dict_age)
print(dict_age)


# clear() function used to delete the data from the dictionary but it will  not free up the memory
new_dict_age.clear()
print(new_dict_age)


# del used to delete entire dictionary from the memory
del dict_age
print(dict_age)  # it will throw an error because the entire dictionary was removed from the memory



