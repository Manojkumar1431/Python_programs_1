#output is stored in C:\Users\91966\PycharmProjects\pythonclass
x=str(input('enter your file name:'))
import os
if os.path.exists(x):
    os.remove(x)
    print('file deleted successfully')
else:
    print('file not found')
