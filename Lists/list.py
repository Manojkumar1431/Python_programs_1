# append,copy
a=list((1,2,3,4))
a.append(8)
b=a.copy()
b.append(5)
print(b)
print(len(a))



# index number
w=list((1,2,3,4))
print(w)
c=int(input('enter avalue:'))
print(w.index(c))



# sort
x=[7,8,5,63,5,67,5,4,6,655,6]
x.sort()
print(x)
print(sorted(x))



# reverse
s=list((1,2,3,4,5,0,6,7,8))
s.sort()
s.reverse()
print(s)



#reverse
d=list(('delhi','manglore','japan','london','lodun','bhupal'))
d.sort()
d.reverse()
print(d)


# insert syntax "list.insert(index_number, value)"
list1 = [1, 2, 5, 7, 8]

list1.insert(2, 9)  # here 2 is Index number and 9 is the value to be inserted into the list
print(list1)