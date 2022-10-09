#prime numbers
n= int(input())
for i in range(1,n+1):
    count=0;
    for j in range(1,n+1):
        if(i%j==0):
            count=count+1
    if(count==2):
            print(i,'prime num');
    else:
            print(i,'not prime');

#check given num is prime or not
n=int(input())
count=0;
for i in range(2,n+1):
    if(n%i==0):
        count=count+1
if(count==1):
    print(n,'is prime');
else:
    print(n,'not prime');




