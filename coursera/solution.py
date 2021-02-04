n = int(input())
arr = [int(i) for i in input().split()]
m = int(input())
mas = [int(i) for i in input().split()]
result = []
s = ''
for i in range(n):
    for j in range(m):
        result.append(abs(arr[i]-mas[j]))
    s += str(result.index(min(result)) + 1) + ' '
    result.clear()
print(*[])
