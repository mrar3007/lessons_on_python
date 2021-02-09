def resultPrint(sSet):
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
resultPrint(mySet)
