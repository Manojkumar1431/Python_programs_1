a = 10
b = 12

if a >= b:
    print("a is greater")
else:
    print("b is greater")

# ================================================================================
# "==" operator usage
if (10 + 2) == (6 + 6):
    print("True")
else:
    print("False")

# =================================================================================
# usage of if condition in Lists
List1 = ['manoj', 'mintu', 'akhil', 'Nikhil']
if 'mintu' in List1:
    print("manoj is in the List1")
else:
    print("manoj is not in the List1")

# ==================================================================================
# usage of if-else conditions in Dictionary
dict1 = {"Name": "Manoj", "address": "WGL", "mobile": 960374}
if 'mobile' in dict1:
    print("mobile element is present in dict1 the value is ", dict1['mobile'])

if not'role' in dict1:  # usage of not keyword
    print("yes role is not listed in dict1")

# ===================================================================================
# Ternary operator
num = 50
num = num-20 if num > 20 else num + 20
print("num = ", num)

# =====================================================================================
# Nested if else block

total = int(input("What is the total amount of your online shopping? "))
country = input("USA / CANADA?  : ")

if country == "USA":
    if total <= 50:
        print("shipping cost is $9.00")
    elif total <= 100:
        print("Shipping cost is $6.00")
    else:
        print("Shipping is Free")
if country == "CANADA":
    if total <= 50:
        print("shipping cost is $12.00")
    elif total <= 100:
        print("Shipping cost is $8.00")
    else:
        print("Shipping is Free")

# ======================================================================================
#
