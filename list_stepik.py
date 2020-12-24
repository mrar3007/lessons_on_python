# s = input()
# arr = s.split()
mas = []
sum = 0

'''
arr = s.split()

for value in arr:
    sum += int(value)

print(sum)
'''

'''
for i in range(0, len(arr)):
    if i == len(arr) - 1:
        if len(arr) == 1:
            mas.append(arr[0])
            break
        sum = int(arr[i - 1]) + int(arr[0])
    else:
        sum = int(arr[i - 1]) + int(arr[i + 1])
    mas.append(str(sum))

s = ' '.join(mas)
print(s)
'''
'''
i = 0
kol = 0
arr.sort()

while i < len(arr):
    kol = arr.count(arr[i])
    if kol > 1:
        mas.append(str(arr[i]))
    i += kol

s = ' '.join(mas)
print(s)
'''


