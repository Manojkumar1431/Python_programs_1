# palindrome number/reverse a number
n=int(input())
dummy=n;
rev=0
while n>0:
        a=n%10;
        rev=rev*10+a;
        n=n//10;
print(rev)
if dummy==rev:print('pal')


#palindrome string/reverse a string
n=str(input())
c=n[::-1]
if n==c:
    print('pal')