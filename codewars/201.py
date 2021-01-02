def disemvowel(str):
    arr = ['a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O']
    return ''.join([i for i in str if arr.count(i) == 0])

print(disemvowel("This website is for losers LOL!"))

