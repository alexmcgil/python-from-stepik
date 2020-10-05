mat = []
x = ''
stroka = 0
stolb = 0
while x!= 'end':
    x = input()
    if x == 'end':
        break
    stroka = len(list(x.split()))
    mat.append(list(x.split()))