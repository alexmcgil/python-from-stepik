def modify_list(l):
    for i in l:
        if l[i] % 2 != 0:
            del l[i]
        else:
            l[i] // 2



