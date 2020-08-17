string = input('Enter String: ')
op,num,var,tok = 0,0,0,0
operators = ['+','-','*','/','^','=','(',')']
for i in range(len(string)):
    if string[i] in operators:
        op += 1
        tok += 1
    elif((ord(string[i])>=48 and ord(string[i])<=57) and (ord(string[i-1])<48 or ord(string[i-1])>57)):
        tok += 1
        num += 1
    elif ord(string[i])>=97 and ord(string[i])<=122:
        var += 1
        tok += 1
print('Operators=',op)
print('Numbers=',num)
print('Variables=',var)
print('Tokens=',tok)
