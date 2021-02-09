fin = open('input.txt', 'r', encoding='utf-8')
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
    print(good[:good.index(good[k - 1])][-1], file=fout)
