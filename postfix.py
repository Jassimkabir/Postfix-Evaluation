def postfix(s):
    stack= []

    for i in s:
        if i.isdigit():
            stack.append(int(i))

        elif i== "+":
            n1= stack.pop()
            n2= stack.pop()
            stack.append(n1+n2)

        elif i== "-":
            n1= stack.pop()
            n2= stack.pop()
            stack.append(n1-n2)

        elif i== "/":
            n1= stack.pop()
            n2= stack.pop()
            stack.append(n1/n2)

        elif i== "*":
            n1= stack.pop()
            n2= stack.pop()
            stack.append(n1*n2)

        else:
            return None    

    return stack[0]
