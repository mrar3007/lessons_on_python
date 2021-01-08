'''def nb_dig(n, d):
	return sum(str(i*i).count(str(d)) for i in range(n+1))
print(nb_dig(11011, 2))	'''

'''def presses(phrase):
    arr = ['', '1ADGJMPTW* #', 'BEHKNQUX0', 'CFILORVY', '23456S8Z', '79']
    return sum(j for i in phrase.upper() for j in range(len(arr)) if arr[j].count(i) > 0)
print(presses("HOW R U"))'''

'''
          My version   
              |||
              VVV
def sum_pairs(ints, s):
    arr = [[ints[i], ints[j]] for i in range(len(ints)) for j in range(len(ints)) if ints[i] + ints[j] == s and i != j]
    return arr[-2] if len(arr) > 1 else arr[0] if len(arr) == 1 else None'''

'''Версия google и немного моя)   
        |||
        VVV'''
def sum_pairs(ints, s):
    arr = set()
    for i in ints:
        diff = s - i
        if diff in arr:
            return [diff, i]
        arr.add(i)

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

print(sum_pairs(l1, 8))
print(sum_pairs(l2, -6))
print(sum_pairs(l3, -7))
print(sum_pairs(l4, 2))
print(sum_pairs(l5, 10))
print(sum_pairs(l6, 8))
print(sum_pairs(l7, 0))
print(sum_pairs(l8, 10))


