arr = [int(i) for i in input().split()]
x = int(input())
c = arr.count(x)

if c != 0:
    y = 0
    while y < len(arr) and c != 0:
        pos = arr.index(x, y)
        print(pos, end=' ')
        c -= 1
        y = pos + 1
else:
    print('Отсутствует')
