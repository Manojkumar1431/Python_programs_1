a = (1, 2, 3, 4, 5, 6)
print(type(a))
print(a)



b = tuple((2, 3, 4, 5, 6))
print(b)

# indexs
a = (1, 2, 3, 4, 5, 6)
print(a.index(2))
for i in a:
    print(i)

# tuple is immutable
# list in tuple is modifiable
x = (1, 2, 34, ['q', 'w', 'r'])
x[3][2] = 'wrong'
print(x)
print(len(x))
