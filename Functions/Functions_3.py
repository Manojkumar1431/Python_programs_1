def func(**kwargs):
    print(type(kwargs))  # here the **kwargs considered in the format of dictionary
    print(kwargs)


func(name='Manoj', college="GNITC")
print("\n")


# ===================================================================

def fun_1(*colleges, **students_roles):
    print("colleges : ", colleges)
    print("students ", students_roles)

fun_1('GNI', 'KITS', 'SR', Manoj='ASE', Mintu="SE")
