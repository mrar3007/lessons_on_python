'''def proper_fractions(n):
    count = 0
    for i in range(1, n):
        arr = [j for j in range(2, i+1) if i % j == 0 and n % j == 0]
        if len(arr) == 0:
            count += 1
    return count
'''

def proper_fractions(n):
    phi = n > 1 and n
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    if n > 1: phi -= phi // n
    return phi

print(proper_fractions(15))
