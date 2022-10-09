# Swap 2 nums using 3rd variable
a,b=10,12
print("before swap",a,b)
temp=a
a=b
b=temp
print("after swap",a,b)



# swap without using 3rd variable
c,d=10,12
print(c,d)
sum=c+d
c=sum-c
d=sum-d
print(c,d)



# given year is leap year or not
y=int(input())
if(y%4==0):
    print(y," is a leap year ")
elif(y%400==0):
    print(y,"is a leap year")
else:
    print("not a leap year")
