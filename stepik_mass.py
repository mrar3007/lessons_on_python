s = ''
mass = []

while True:
    s = input()
    if s == 'end':
        break
    mass.append([int(i) for i in s.split()])

li, lj = len(mass), len(mass[0])

new = [[sum([mass[i-1][j], mass[(i+1)%li][j], mass[i][(j+1)%lj], mass[i][j-1]]) for j in range(lj)] for i in range(li)]

for i in range(li):
    for j in range(lj):
        print(new[i][j], end=' ')
    print()

