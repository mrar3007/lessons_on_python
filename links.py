
list = ['apple', 'juice', 'orange']
copy = list

del list[0]

print(list)
print(copy)

copy = list[:]
del copy[0]

print(list)
print(copy)
