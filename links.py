
s = input()
count = 1
b = ''

for i in range(0, len(s)):
    if i != len(s)-1:
        if s[i] == s[i + 1]:
            count += 1
        else:
            b += s[i] + str(count)
            count = 1
    else:
        b += s[i] + str(count)
        break

print(b)
