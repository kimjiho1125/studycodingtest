while True:
    D = input()
    if D == '.':
        break

    stack = []
    temp = True

    for p in D:
        if p == '(' or p =='[':
            stack.append(p)
        elif p == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif p == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print("yes")
    else:
        print("no")
