'''def disemvowel(str):
    arr = ['a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O']
    return ''.join([i for i in str if arr.count(i) == 0])

print(disemvowel("This website is for losers LOL!"))'''

'''def filter_list(l):
    return [i for i in l if type(i) is int]

print([1, 2, 'a', 'b'])'''

'''def longest(s1, s2):
    s = sorted(s1 + s2)
    return ''.join([s[i] for i in range(len(s)) if s[i] != s[i-1]])

print(longest("aretheyhere", "yestheyarehere"))
'''

'''def count_smileys(arr):
    return sum([1 for i in arr if (i[0] == ':' or i[0] == ';') and (i[1] == i[len(i)-1] or i[1] == '~' or i[1] == '-') and (i[len(i)-1] == 'D' or i[len(i)-1] == ')')])
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))'''

def tickets(people):
    cashier = {25: 0, 50: 0, 100: 0}
    for i in range(len(people)):
        if people[i] == 25:
            cashier[25] += 1
        elif people[i] == 50:
            if cashier[25] >= 1:
                cashier[25] -= 1
            else:
                return "No"
            cashier[50] += 1
        elif people[i] == 100:
            if cashier[25] >= 3:
                cashier[25] -= 3
            elif cashier[25] >= 1 and cashier[50] >= 1:
                cashier[25] -= 1
                cashier[50] -= 1
            else:
                return "No"
            cashier[100] += 1
    return "Yes"

print(tickets([25, 25, 50, 50, 100]))