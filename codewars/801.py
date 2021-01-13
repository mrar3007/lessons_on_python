def decrypt(ds, n):
    if n <= 0:
        return ds
    return decrypt(ds, 4-n)


def encrypt(s, n):
    if n <= 0:
        return s
    result, l, x = '', len(s), 1
    for i in range(n):
        for j in range(2):
            result += ''.join([s[y] for y in range(x, l, 2)])
            x = 0 if x == 1 else 1
        s = result
        result = ''
    return s if l % 2 == 1 else ''.join(reversed([i for i in s]))

print(encrypt('This is a test!!',3))
#print(decrypt(" Tah itse sits!", 3))
#print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))
print(encrypt(" Tah itse sits!", 1))
