# empty dictionary
fruits = {}
print(fruits)


fruits['apple'] = 20
fruits['mango'] = 30
fruits['banana'] = 40
fruits['dragon_fruit'] = 50

print(fruits)


# ======================================================================================================================


# created Dictionary and mentioned keys in the form of Dictionary
fruits1 = {
    'almonds': {'Monday': 30, 'Tuesday': 40, 'Wednesday': 60},
    'Berry': {'Monday': 50, 'Tuesday': 60, 'Wednesday': 30},
    'carrot': {'Monday': 80, 'Tuesday': 30, 'Wednesday': 90},
    'Orange': {'Monday': 40, 'Tuesday': 60, 'Wednesday': 40}
    }

print(fruits1['almonds']['Tuesday'])

print(fruits1['carrot']['Monday'])

# modifying
fruits1['Orange']['Wednesday'] = 80
print(fruits1)




