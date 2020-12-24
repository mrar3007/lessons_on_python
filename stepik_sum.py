arr = []
result = 0
summa = 1

while summa != 0:
    summa = 0
    num = int(input())
    arr.append(num)
    summa = sum(arr)

for value in arr:
    result += value**2

print(result)
