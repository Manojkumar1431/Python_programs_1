def manoj(a, b):
    return a+b
x = manoj(b=10,a=20,)
print(x)

print("\n")
def mintu(a,b,c=10):
    print("sum is ", a+b+c);

a = mintu(20, 30, 40)

print("\n")
def fun(a=10,b=30):
    print("sum is ",a+b)
s = fun()

def myfun(*names):
    for name in names:
        print(f'hello{name}')
b = myfun('manoj','mintu')
