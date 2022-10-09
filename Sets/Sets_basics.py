set1 = {1, 2, 3, 1, 4, 5, 2}
print(set1)  # No duplicates are allowed


# we can contain tuple,boolean,Strings,Integers in a Set but not Lists and Dictionary types because they are mutable
# Sets does not support index so we cannot retrieve any element by their index
set2 = {'manoj', 'Mintu', 'abc', 1.2, 3, True, (1, 3, 5), 'Nikhil'}
print(set2)  # Sets are un-ordered

set2.add('Ranjith')
print(set2)

'''discard and remove functions will remove the specified element,
the main difference is if you specify an already removed element
discard will print nothing but where as remove function will throw an error 
'''
set2.discard('Nikhil')
print(set2)

set2.remove('abc')
print(set2)


# clear() is used to delete data from the set
#set2.clear()