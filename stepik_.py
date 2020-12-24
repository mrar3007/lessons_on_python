n, m, k = (int(i) for i in input().split())
array = [[0 for j in range(m)] for i in range(n)]

for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    array[row][col] = -1
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and array[ai][aj] == -1:
                        array[i][j] += 1

for i in range(n):
    for j in range(m):
        if array[i][j] == -1:
            print('*', end='')
        elif array[i][j] == 0:
            print('.', end='')
        else:
            print(array[i][j], end='')
    print()
