data = int(input())
sum1 = 0
count = 0
if data <= 0:
    print("invalid input")
else:
    while data > 0:
        a = data % 10
        for i in range(2, data+1):
            if a % i == 0:
                count = count+1
            if count == 1:
                sum1 = sum1 + a
            else:
                continue
        data = data//10
print(sum1)


