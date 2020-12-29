'''def closest_mod_5(x):
    y = x
    if y % 5 == 0:
        return y
    while y % 5 != 0:
        y += 1
    return y

print(closest_mod_5(5))
print(closest_mod_5(7))'''

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
