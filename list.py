list = ['apple', 'orange', 'banana']

print('list - output list\nexit - quit from program\nsort - sort list\n'
      'del - delete value element')

while True:
    print('')
    str = input('Введите слово для добавления в список: ')
    if str == 'exit':
        break
    elif str == 'list':
        print(list)
        continue
    elif str == 'sort':
        print('Before sort => ', list)
        list.sort()
        print('After sort => ', list)
    elif str == 'del':
        print(list)
        a = int(input('Введите номер удаленённой переменной: ')) - 1
        del list[a]
        print(list)
    else:
        list.append(str)
