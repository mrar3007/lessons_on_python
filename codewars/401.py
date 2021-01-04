'''def printer_error(s):
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    return '{0}/{1}'.format(len(s) - sum([1 for i in s for j in arr if i == j]), len(s))

print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))
'''

def remove_char(s):
    #your code here
    return s[1:-1]
print(remove_char('rust'))

