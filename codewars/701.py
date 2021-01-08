'''def Xbonacci(signature,n):
    #your code here
    l = len(signature)
    if n >= l:
        for i in range(l, n):
            signature.append(sum(signature[-l:]))
        return signature
    return signature[:n]

print(Xbonacci([1,0,0,0,0,0,0,0,0,0],20))'''


def order_weight(s):
    mass = []
    arr = [[int(j) for j in i] for i in s.split()]
    l = len(arr)
    kol = 0
    for i in range(l):
        for j in range(l - 1, i, -1):
            if sum(arr[j]) < sum(arr[i]):
                arr[i], arr[j] = arr[j], arr[i]
            if sum(arr[j]) == sum(arr[i]):
                kol += 1
    s = ''
    for i in arr:
        for j in i:
            s += str(j)
        mass.append(s)
        s = ''
    return ' '.join(mass)

print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))



