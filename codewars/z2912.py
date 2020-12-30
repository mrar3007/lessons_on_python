'''def closest_mod_5(x):
    y = x
    if y % 5 == 0:
        return y
    while y % 5 != 0:
        y += 1
    return y

print(closest_mod_5(5))
print(closest_mod_5(7))'''
'''
def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print(s(11, 10))
s(11, b=20)
s(5, 5, 5, 5, 1)
s(21)
s(11, 10)
'''
'''
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print(fib(2))
'''
'''def C(n, k):
    return 1 if k == 0 else 0 if k > n else C(n-1, k) + C(n-1, k-1)

n, k = map(int, input().split())
print(C(n, k))
'''
'''
def add(nmsp, var):
    dict[nmsp]['vars'].append(var)

def create(nmsp, parent):
    dict[nmsp] = {'parent': parent,'vars': []}

def get(nmsp, var):
    if nmsp == None:
        return None
    parent = dict[nmsp]['parent']
    c = dict[nmsp]['vars'].count(var)
    return nmsp if c > 0 else get(parent, var)

dict = {
    'global': {
        'parent': None,
        'vars': []
    }
}

arr = []
n = int(input())
while n != 0:
    cmd, nmsp, var = input().split()
    if cmd == 'add':
        add(nmsp, var)
    elif cmd == 'get':
        arr.append(get(nmsp, var))
    else:
        create(nmsp, var)
    n -= 1

for i in arr:
    print(i, end='\n')
'''


