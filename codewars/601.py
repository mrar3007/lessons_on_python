'''def nb_dig(n, d):
	return sum(str(i*i).count(str(d)) for i in range(n+1))
print(nb_dig(11011, 2))	'''

def presses(phrase):
    arr = ['', '1ADGJMPTW* #', 'BEHKNQUX0', 'CFILORVY', '23456S8Z', '79']
    return sum(j for i in phrase.upper() for j in range(len(arr)) if arr[j].count(i) > 0)
print(presses("HOW R U"))

