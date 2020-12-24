
def reverseMass(num):
    mass = list(num)
    mass.sort()
    mass.reverse()
    st = ''.join(mass)
    return st

print(reverseMass('5463214598'))
