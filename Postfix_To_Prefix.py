def Postfix_to_prefix(p): 
    for i in p:
        if i.isalnum():
            s.append(i)
        else:
            a = s.pop()
            b = s.pop()
            k = i + b + a
            s.append(k)
expression = input()
s = []
Postfix_to_prefix(expression)
print(*s)