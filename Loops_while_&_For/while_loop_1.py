# general usage of while loop
i = 1
while i < 6:
    print(i)
    i += 1

# =======================
# break statement
print('Break statement example')
j = 1
while j < 6:
    print(j)
    if j == 3:
        break
    j = j+1

# =====================================
# continue statement
print('Continue statement Example')
k = 1
while k <= 6:
    k += 1
    if k == 3:
        continue
    print(k)