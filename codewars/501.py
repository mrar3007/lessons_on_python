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

'''def namelist(names):
    s = ''
    for i in names:
        if len(names) == 1:
            return i['name']
        elif names.index(i) == len(names)-2:
            j = names.index(i)
            s += names[j]['name']
            s += ' & ' + names[j+1]['name']
            break
        s += i['name'] + ', '
    return s

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))'''

'''def open_or_senior(data):
    return ["Senior" if i[0] > 54 and i[1] > 7 else "Open" for i in data]
print(open_or_senior([[1, 1], [55, 8]]))'''




