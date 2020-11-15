killeri = []
def modify_list(l):
    le = len(l)
    for i in range(0,le):
        if l[i] % 2 != 0:
            killeri.append(i)
    for i in killeri:
        del l[i]
    le = len(l)
    for i in range(0, le):
        if l[i] % 2 == 0:
            l[i] // 2
