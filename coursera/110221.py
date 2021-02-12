myDict = {}
with open('input.txt', 'r', encoding='utf-8') as fin:
    for line in fin.readlines():
        arr = line.split()
        if arr[0] not in myDict:
            myDict[arr[0]] = {arr[1]: int(arr[2])}
        elif arr[1] not in myDict[arr[0]]:
            myDict[arr[0]].setdefault(arr[1], int(arr[2]))
        else:
            myDict[arr[0]][arr[1]] += int(arr[2])

for item in sorted(myDict.items()):
    print(item[0], end=':\n')
    elem = sorted(dict(item[1]).items())
    for value in elem:
        print(value[0], value[1])
