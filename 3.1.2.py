def modify_list(l):
    le = len(l)
    for i in range(0,le):
        if l[i] % 2 != 0:
            del l[i]
    le = len(l)
    for i in range(0, le):
        if l[i] % 2 == 0:
            l[i] // 2



