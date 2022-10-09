# print numbers from 1 to userinput

n=int(input())
for i in range (1,n+1):
    print(i)



# print  A-Z

for i in range (97,122+1):
    print(chr(i))


# print given num is odd or even
a=int(input())
if(a%2==1):
    print("given num",a,"is odd")
else:
    print("given num",a,"is even")


# print all odd nums
for i in range (0,100):
    if(i%2==1):
        print(i)


