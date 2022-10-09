#output is stored in C:\Users\91966\PycharmProjects\pythonclass
v=str(input('enter file name:'))
if v.endswith('.txt'):


        file=open(v,'w')
        print('file found')
        b = input('enter content in file:\n')
        file.write(b)
        file.close()
        print('successfully entered value')
else:
    print('file not found')


