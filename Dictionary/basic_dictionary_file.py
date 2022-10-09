dict1 = {
    'name': 'mintu',
    'mobile':  989830948,
    'addr': 'wgl',
    'role': 'software developer'
    }

# retrieving one key from dict1
print(dict1['name'])

# Retrieve all keys from dict1
print(dict1.keys())

# check with "in" key word whether name is present in dict1 or not
print('name' in dict1.keys())

# Retrieve all values from dict1
print(dict1.values())


# ============================================================================================================

# dictionary contains all kinds of data types
mixed_dict = {
    False: 'manoj',
    'interest': ['badminton', 3, 4],
    'isClever': True
}
print(mixed_dict)
print(mixed_dict['interest'])
print(mixed_dict.keys())
print(mixed_dict.values())

# ===================================================================================================================

bike_info = {
    'model': 'R15V4',
    'color': 'Red',
    'year': '2022',
    'price': 206000
    }

# inserting new field ito dictionary
bike_info['Date of purchase'] = '20/1/2022'
print(bike_info)

# updating/modifying
bike_info['model'] = 'Apache RR 310'
print(bike_info)

# delete function
del bike_info['price']
print(bike_info)




