s, n = (int(i) for i in input().split())
arr = sorted(int(input()) for i in range(n))
count = 0
for i in range(len(arr)):
    if sum(arr[:i+1]) <= s:
        count += 1
print(count)
