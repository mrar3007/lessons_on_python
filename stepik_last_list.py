def modify_list(lst):
    i = 0
    l = len(lst)
    lst.sort()
    while i < l:
        x = lst[i]
        if x % 2 != 0:
            del lst[i]
            l -= 1
        else:
            lst[i] = x // 2
            i += 1

lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)
modify_list(lst)
print(lst)