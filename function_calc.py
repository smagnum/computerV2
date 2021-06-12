def function_calc(eq, x) :
    eq = eq.replace(" ", "")
    # 3 + 4(x + 2) + 5(3 + 2(x+1))
    num = ''
    tab = []
    length = len(eq)
    i = 0
    parenthese = 0
    while i < length :
        
        if eq[i] == '(' :
            parenthese += 1
            num += eq[i]
        elif eq[i] == ')' :
            parenthese -= 1
            num += eq[i]
            tab.append(num)
        elif parenthese == 0 and (eq[i] == '%' or eq[i] == '*' or eq[i] == '/' or eq[i] == '+' or eq[i] == '-') : 
            tab.append(num)
            tab.append(eq[i])
            num = ''
        else:
            num += eq[i]
            if i == length - 1:
                tab.append(num)
        i += 1
    return tab



print (function_calc("3 + 4(x + 2) + 5(3 + 2(x+1))", 'x'))


