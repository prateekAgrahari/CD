n = int(input('How many productions: '))
d = {}
for i in range(n):
    head,equal,prodn = [str(x) for x in input().split()]
    d[head] = prodn

ele = input('Enter element: ')
tmp = d[ele][0]
if tmp.isupper():
    while tmp.isupper():
        tmp = d[tmp][0]
    print(tmp)
else:
    print(tmp)
