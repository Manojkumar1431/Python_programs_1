"""
basically when we open a file we generally forget to close it,
so there will be a loss of memory and also it relies to a type of vulnerability ,
in order to overcome it we use
              "with open(file_name) as f:"
so it automatically closes the the file after its use is done
"""

with open('C:/Users/91966/Desktop/python text files/file3.txt') as f:
    line = f.readline()

    while line:
        print(line)
        line = f.readline()

# checking whether the file is closed or not
print(f.closed)
