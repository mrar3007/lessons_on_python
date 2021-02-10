myDict = {}
with open('input.txt', 'r', encoding='utf-8') as fin:
    for i in fin.readlines():
        for j in i.split():
            myDict[j] = myDict.get(j, 0) + 1
result = sorted(myDict.items(), key=lambda item: item[1], reverse=True)
myDict = {i: [] for i in range(1, int(result[0][1]) + 1)}
for i in result:
    myDict[i[1]].append(i[0])
result.clear()
for item in myDict.values():
    result += sorted(item, reverse=True)
for i in range(len(result)-1, -1, -1):
    print(result[i])
