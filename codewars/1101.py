def solution(args):
    s = ''
    l = len(args)
    k = 0
    for x in range(l):
        if k > 0:
            k -= 1
            continue
        if x < l-3:
            if args[x+2] - args[x] == 2:
                s += str(args[x]) + '-'
                if x == l - 4:
                    s += str(args[l - 1])
                    break
                for i in range(x, l-2):
                    if args[i+1]-args[i]!=1:
                        s += str(args[i]) + ','
                        print(s)
                        break
                    k += 1
        s += str(args[x]) + ','
    return s

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
print(solution([-3,-2,-1,2,10,15,16,18,19,20]))



