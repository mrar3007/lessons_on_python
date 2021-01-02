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
