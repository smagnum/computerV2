
def simpli_A(tab, number) :
    tab = list(tab)
    print (tab)

    res = []
    num = ''
    for chunk in tab :
        try :
            int(chunk)
            num += chunk
            if '-' in num :
                num = int(num)
            elif '+' in num :
                num = num.replace('+', '')
            
            tab[tab.index(chunk)] = num
            eq = int(num) * int(number)
            res.append(eq)
        except :
            if chunk == '+' or chunk == '-':
                num += chunk
                tab[tab.index(chunk)] = ''
            else :
                res.append(number+chunk)
    return res


def simpli_B(tab) :
    tab = list(tab)
    print (tab)

    res = []
    num = ''
    for chunk in tab :
        try :
            print ()
            print(chunk)
            print()
            int(chunk)
            num += chunk
            print (num)
            if '-' in num :
                num = int(num)
            elif '+' in num :
                num = num.replace('+', '')
            
            tab[tab.index(chunk)] = num
            res.append(num)
        except :
            if chunk == '+' or chunk == '-':
                num += chunk
                tab[tab.index(chunk)] = ''
            else :
                res.append(chunk)
    return res

def multiple (tab, number) :
    # try :
    #     int(number)
    #     print ('ok')
    # except :
    #     print ('Do boucle ')
    nums = list(number)
    nums = simpli_B(nums)
    for num in nums :
        print (num)
    #res = simpli_A(tab, nums)
    # res2 = simpli_B(tab)
    # res = simpli_A(tab, number)
    
    # print ('Result here')
    # print (res)
    # print (res2)
    # tab = list(tab)
    # print (tab)

    # res = []
    # num = ''
    # for chunk in tab :
    #     try :
    #         int(chunk)
    #         num += chunk
    #         if '-' in num :
    #             num = int(num)
    #         elif '+' in num :
    #             num = num.replace('+', '')
            
    #         tab[tab.index(chunk)] = num
    #         eq = int(num) * int(number)
    #         res.append(eq)
    #     except :
    #         if chunk == '+' or chunk == '-':
    #             num += chunk
    #             tab[tab.index(chunk)] = ''
    #         else :
    #             res.append(number+chunk)


                
   
    # print (tab)    
    # print (res)



multiple("y-1", "2+3")

def reduce_parenthese (paranthese_number, x) :
    param = list(paranthese_number)
    print (param)
    length = len(param)
    i = 0

    parenthese = 0
    num = ''
    while i < length :
        if param[i] == '(' :
            parenthese += 1
            open_index = i
        elif param[i] == ')' :
            per = param[open_index + 1:i]
            print ('here')
            print (per)
            print ('endhere')

            try :
                float(param[open_index - 1])
                
                if x in param[open_index:i+1] :
                    print ('yesy')
                    num += param[open_index - 1] + x

            except :
                num += param[open_index - 1] + x
            
            parenthese -= 1

        
        print (param[i])
        i += 1
    print (num)

#reduce_parenthese("5(3+2(y+1))", 'y')

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
            print ('1')
            parenthese += 1
            num += eq[i]
        elif eq[i] == ')' :
            print (2)
            parenthese -= 1
            num += eq[i]
            # if parenthese == 0 :
            #     tab.append(num)
        elif parenthese == 0 and (eq[i] == '%' or eq[i] == '*' or eq[i] == '/' or eq[i] == '+' or eq[i] == '-') : 
            print (3)
            tab.append(num)
            tab.append(eq[i])
            num = ''
        else:
            print (4)
            num += eq[i]
            if i == length - 1:
                tab.append(num)
        i += 1
    
    # for t in tab :
    #     if '(' in t :
    #         print (res)

    return tab


# print (function_calc("3+1(2+3)-", 'y'))
# print (function_calc("3 + 4(y + 2) + 5(3 + 2(y+1)) - 2", 'y'))


