fruits = ['apple', 'banana', 'carrot']

for x in fruits:
    print(x)

for i in 'banana':
    print(i)

# ================================================================
# range() function
print('range() function usage')
for k in range(6):
    print(k)

print('range function with parameters')
for l in range(1, 4):  # here range(start int, stop int)
    print(l)

print('range function with step size')
for m in range(1, 10, 2):
    print(m)

# ===================================================================
print('ELse in for loop')
for a in range(6):
    print(a)
else:
    print("finally finished")

# ====================================================================
print('Nested loops')
adj = ['red', 'big', 'tasty']
obj = ['scale', 'pen','pencil']
for o in adj:
    for p in obj:
        print(o, p)
