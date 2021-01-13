'''def solution(s, markers):
    s = [i for i in s]
    res = []
    com = True
    for i in range(len(s)):
        if s[i] in markers:
            com = False
            for j in range(i - 1, 0, -1):
                if len(res) > 0:
                    if s[j] == ' ' and res[-1] == ' ':
                        del res[-1]
                    else:
                        break
        elif s[i] == '\n':
            com = True
        if com == True:
            res.append(s[i])
    return ''.join(res)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("a #b\nc\nd $e f g", ["#", "$"]))
print(solution('cherries\n^ = watermelons\n, bananas lemons watermelons strawberries\navocados oranges lemons', ['-', '=', ',', '!', '^', "'", '#']))
'''

'''def anagrams(word, words):
    arr = []
    obj = {}
    obj1 = {}
    count = 0
    for i in word:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    for i in words:
        for j in i:
            if j in obj1:
                obj1[j] += 1
            else:
                obj1[j] = 1
        print(obj1)
        for j in obj1:
            if j in obj:
                if obj1[j] == obj[j]:
                    count += 1
            else:
                break
        if count == len(obj):
            arr.append(i)
        obj1 = {}
        count = 0
    return arr

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))'''

# 'years': 0, 'days': 0, 'hours': 0, 'minutes': 0,  'seconds': 0

def format_duration(seconds):
    obj = {}
    num = seconds // 31536000
    if num > 0:
        key = 'years' if num >= 2 else 'year'
        obj[key] = num
        seconds -= obj[key]*31536000
    num = seconds // 86400
    if num > 0:
        key = 'days' if num >= 2 else 'day'
        obj[key] = num
        seconds -= obj[key] * 86400
    num = seconds // 3600
    if num > 0:
        key = 'hours' if num >= 2 else 'hour'
        obj[key] = num
        seconds -= obj[key] * 3600
    num = seconds // 60
    if num > 0:
        key = 'minutes' if num >= 2 else 'minute'
        obj[key] = num
        seconds -= obj[key] * 60
    key = 'seconds' if seconds >= 2 else 'second'
    obj[key] = seconds
    arr = [str(value) + ' ' + str(key) for key, value in obj.items() if value > 0]
    l = len(arr)
    return 'now' if l > 0 else ''.join([arr[i]+', ' if l >= 3 and i <= l-3 else arr[i]+' and ' if (l >= 3 and i == l-2) or (l == 2 and i == 0) else arr[i] for i in range(l)])

print(format_duration(3601265))
