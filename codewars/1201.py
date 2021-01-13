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

def anagrams(word, words):
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

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))


