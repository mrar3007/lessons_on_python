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

'''def func(f, n):
    if f[1] == '*':
        return f[0] * n
    elif f[1] == '+':
        return f[0] + n
    elif f[1] == '-':
        return n - f[0]
    else:
        return n // f[0]

def zero(f = 0): #your code here
    n = 0
    if type(f) is list:
        return func(f, n)
    return n
def one(f = 0): #your code here
    n = 1
    if type(f) is list:
        return func(f, n)
    return n
def two(f = 0): #your code here
    n = 2
    if type(f) is list:
        return func(f, n)
    return n
def three(f = 0): #your code here
    n = 3
    if type(f) is list:
        return func(f, n)
    return n
def four(f = 0): #your code here
    n = 4
    if type(f) is list:
        return func(f, n)
    return n
def five(f = 0): #your code here
    n = 5
    if type(f) is list:
        return func(f, n)
    return n
def six(f = 0): #your code here
    n = 6
    if type(f) is list:
        return func(f, n)
    return n
def seven(f = 0): #your code here
    n = 7
    if type(f) is list:
        return func(f, n)
    return n
def eight(f = 0): #your code here
    n = 8
    if type(f) is list:
        return func(f, n)
    return n
def nine(f = 0): #your code here
    n = 9
    if type(f) is list:
        return func(f, n)
    return n

def plus(f): #your code here
    return [f, '+']
def minus(f): #your code here
    return [f, '-']
def times(f): #your code here
    return [f, '*']
def divided_by(f): #your code here
    return [f, '//']

print(one(plus(one())))
print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))'''
