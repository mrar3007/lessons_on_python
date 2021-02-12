'''def resultPrint(sSet):
    print(len(sSet))
    for i in sorted(sSet):
        print(i, end='\n')


n = int(input())
arr = [set() for i in range(n)]
mySet = set()
for i in range(n):
    m = int(input())
    for j in range(m):
        arr[i].add(input())
    if i > 0:
        mySet &= arr[i]
        continue
    mySet |= arr[i]
resultPrint(mySet)
mySet = set()
for i in arr:
    mySet |= i
resultPrint(mySet)'''


'''candidates = {}
count = 0
with open('input.txt', 'r', encoding='utf-8') as fin:
    for name in fin.readlines():
        candidates[name.strip()] = candidates.get(name.strip(), 0) + 1
        count += 1
    result = sorted(candidates.items(), key=lambda p: p[1])

with open('output.txt', 'w', encoding='utf-8') as fout:
    if int(result[-1][1]) > count // 2:
        print(result[-1][0], file=fout)
    else:
        print(result[-1][0], file=fout)
        print(result[-2][0], file=fout)'''

'''fin = open('input.txt', 'r', encoding='utf-8')
fout = open('output.txt', 'w', encoding='utf-8')
k = int(fin.readline())
students = [list(map(str, line.split())) for line in fin]
good = []

for i in students:
    if int(i[-3]) >= 40 and int(i[-2]) >= 40 and int(i[-1]) >= 40:
        good.append(int(i[-3])+int(i[-2])+int(i[-1]))

good.sort(reverse=True)

if len(good) <= k:
    print(0, file=fout)
elif good.count(good[0]) > k:
    print(1, file=fout)
elif good[k:].count(good[k - 1]) < 1:
    print(good[:k][-1], file=fout)
else:
    print(good[:good.index(good[k - 1])][-1], file=fout)'''
