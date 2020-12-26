d = {}
arr = [i for i in input().lower().split()]



'''
for value in arr:
    if d.get(value) == None:
        d[value] = 1
    else:
        for key in d:
            if value == key:
                d[key] += 1

for key, value in d.items():
    print(key, value, end='\n')

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key * 2 in d:
        d[key * 2].append(value)
    else:
        d[key * 2] = [value]

d = {}
update_dictionary(d, 1, -1)
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)


dict = {
    'Arkadiy': 179,
    'Igor': 178,
    'Maksim': 165
}

while True:
    print('\nadd - add data\nexit - quit from program\ndel - delete value element\n'
          'anything - output dict\ncount - count name')
    str = input('Введите команду: ')
    if str == 'exit':
        break
    elif str == 'del':
        print(dict)
        name = input('Введите имя: ')
        del dict[name]
        print(dict)
    elif str == 'add':
        print(dict)
        name = input('Введите имя: ')
        high = input('Введите рост: ')
        dict[name] = high
        print(dict)
    elif str == 'count':
        print(dict)
        print('Всего в списке: ', len(dict), ' человек')
    else:
        for name, high in dict.items():
            print('У {0} рост {1}'.format(name, high))

print('program complete')
'''
