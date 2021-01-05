'''def ROT13(s):
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    mass = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
    s = [i for i in s]
    for i in range(len(s)):
        for j in range(13):
            if arr[j] == s[i]:
                s[i] = mass[j]
            elif s[i] == mass[j]:
                s[i] = arr[j]
            elif arr[j] == s[i].lower():
                s[i] = mass[j].upper()
            elif s[i].lower() == mass[j]:
                s[i] = arr[j].upper()
    return ''.join(s)

print(ROT13('Hello'))'''


