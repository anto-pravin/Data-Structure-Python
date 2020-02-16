#Input : ab((cd)((z)
#Output : ab(cd)(z)



string = input()
stack = []
List = []
j = -1
i = 0
while i < len(string):
    if string[i].isalpha():
        stack.append(string[i])
        i += 1
    elif string[i] == '(':
        List.append(string[i])
        if i+1 <= len(string) - 1:
            i += 1
        else:
            break
        while string[i] != ')':
            if string[i] != '(':
                List.append(string[i])
            if i+1 <= len(string) - 1:
                i += 1
            else:
                break
        if string[i] == ')':
            List.append(string[i])
            stack.append(''.join(List))
            List = []
            i += 1
        else:
            for p in List:
                if p.isalpha():
                    stack.append(p)
    else:
        i += 1
print(''.join(stack))