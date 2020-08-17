operators = set(['+','-','*','/','^','(',')'])
priority = {'^':1,'*':2,'/':2,'+':3,'-':3}

def infixToPostfix(exp):
    stack = []
    output = ''
    for ch in exp:
        if ch not in operators:
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1]!='(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[ch]>=priority[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output

exp = input("Enter Infix Expression: ")
print("Infix expression:",exp)
post = infixToPostfix(exp)
print("Postfix expression:",post)
exp = exp[::-1]
pre = infixToPostfix(exp)
pre = pre[::-1]
print("Prefix expression:",pre)
