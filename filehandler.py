file=open('C:/manoj.txt','r')
x=input("enter your content:")
file.write('\n' + x)
file.close()
print('updated successfully')