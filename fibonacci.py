n = int(input())
count = 2
b, c = 0, 1
print(b, c, sep="\n")
while count < n:
    sum = b+c
    b = c
    c = sum
    print(sum)
    count = count+1
