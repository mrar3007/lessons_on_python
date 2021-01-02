arr = []
s = {}
n = int(input())
for i in range(n):
    arr = [i for i in input().split() if i != ':']
    if len(arr) > 1:
        s[arr[0]] = arr[1:]
    else:
        s[arr[0]] = 'object'
arr.clear()
n = int(input())
for i in range(n):
    arr += [i for i in input().split()]
print(arr)
i = 0
j = 1
while i <= n:
    abc = s[arr[j]]
    print(abc)
    x = len(abc) - 1
    while True:
        if abc.count(arr[i]) > 0:
            print('Yes')
            break
        elif s[abc].count(arr[i]) > 0:
            print('Yes')
            break
        elif abc == 'object' or s[abc] == 'object':
            print('No')
            break
        else:
            if x < 0:
                abc = s[arr[j]][x]
                x -= 1
    i += 2
    j = i + 1
