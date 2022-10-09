city = 'Welcome to Hyderabad'

print('length of city', len(city))

# startswith() function
print(city.startswith('W'))

# endswith() function
print(city.endswith('d'))

# count() function
print(city.count('e'))

# lower() & upper() functions
lower_city = city.lower()
print(lower_city)

upper_city = city.upper()
print(upper_city)

# find() function
print(city.find('e'))

print(city.index('e'))

# split() function
print(city.split('e'))

print(city.split(' '))  # split space

# join() function
join_city = city.split(' ')
print(join_city)

print(','.join(join_city))

print('|'.join(join_city))

asterisk = '*'  # declaring asterisk separately and calling in the join function without directly declaring
print(asterisk.join(join_city))

