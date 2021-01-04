'''def printer_error(s):
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    return '{0}/{1}'.format(len(s) - sum([1 for i in s for j in arr if i == j]), len(s))

print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))
'''

'''def remove_char(s):
    #your code here
    return s[1:-1]
print(remove_char('rust'))
'''

'''def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"
print(odd_or_even([0, 1, 2]))'''