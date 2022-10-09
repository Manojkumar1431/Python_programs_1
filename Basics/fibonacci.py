n = int(input())
count = 2
b,c=1,2
while count < n:
    sum=b+c
    b=c
    c=sum
    count=count+1
    print(sum)