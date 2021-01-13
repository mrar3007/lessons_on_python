def solution(s, markers):
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







