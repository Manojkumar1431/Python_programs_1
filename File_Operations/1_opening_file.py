file1 = open('C:/Users/91966/Desktop/python text files/Text_file.txt')

print(file1.read())  # to read the text from the file

print(file1.read(5))  # it will print first five bytes of the file

print(file1.mode)  # to read the permission given to the file whether read/write

print(file1.name)  # to print the name of the file

print(file1.closed)  # to know the status of file whether open/close, True = file is closed, False = file is opened

print(file1.tell())  # it will tell to which position the cursor is pointing to

file1.close()

print(file1.closed)

# ================================================================================================================
# understanding of tell() and seek() operations
file2 = open('C:/Users/91966/Desktop/python text files/file2.txt')

print(file2.tell())  # tells where the cursor is pointed

print(file2.read(5))  # reads 5 bytes from the cursor pointing onwards

print(file2.tell())  # now knowing the cursor position in the text file

print(file2.read(5))  # again read the 5 bytes from the cursor pointing onwards

print(file2.seek(0))  # moving the cursor to first position by mentioning seek(0)

print(file2.read(5))  # again reading 5 bytes from the file

print(file2.seek(0))
# print(file2.readline())
print(file2.readlines())
