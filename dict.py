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
