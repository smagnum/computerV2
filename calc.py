# 3 + 4(5 + 6(7-8(9*10) - 3 / 7) - 6*4)-3+1

# def my_eval(x) :
#     x = x.replace(" ", "")
#     x = list(x)

#     # Modulo %
#     i = 0
#     length = len(x)
#     if '%' in x :
#         while i < length :
#             if x[i] == '%' :
#                 res = int (x[i-1]) % int (x[i+1])
#                 print (res)
#                 x[i-1 : i+2] = str(res)
#                 length = len(x)
#                 i = 0
#                 print (x)
#             i += 1
    
#     # Multiplication *
#     if '*' in x :
#         i = 0
#         length = len(x)
#         while i < length :
#             if x[i] == '*' :
#                 res = int (x[i-1]) * int (x[i+1])
#                 print (res)
#                 x[i-1 : i+2] = ''
#                 x[i] = str(res)
#                 length = len(x)
#                 i = 0
#                 print (x)
#             i += 1

#     x = ''.join(x)
#     print (x)

def clean(tab) :
    length = len(tab)
    i = 0
    while i < length :
        if tab[i] == '#' or tab[i] == '' :
            tab.remove(tab[i])
            length = len(tab)
            i = 0
        i += 1
    return tab


def my_eval(x) :
    x = x.replace(" ", "")
    length = len(x)
    i = 0
    num = ''
    tab = []
    while i < length :
        if x[i] == '%' or x[i] == '*' or x[i] == '/' or x[i] == '+' or x[i] == '-' : 
            tab.append(num)
            tab.append(x[i])
            num = ''
        else :
            num += x[i]
            if i == length -1 :
                tab.append(num)
        i += 1

    tab = clean(tab)
    # God of %
    length = len(tab)
    i = 0
    while i < length :
        # Multiplication
        if tab[i] == '%' :
            print (tab)
            
            try : 
                float(tab[i+1])
                print ()
                print ('********')
                print (tab)
                print ('********')
                print ()
                if tab[i-2] == '-' :
                    res = -1 * float(tab[i-1]) % float(tab[i+1])
                    tab[i-2] = '#'
                else :
                    res = float(tab[i-1]) % float(tab[i+1])
                tab[i-1] = '#'
                tab[i+1] = str(res)
                tab[i] = '#'
            except :
                print ()
                print (tab[i-1])
                print (tab[i])
                print (tab[i+1])
                print (tab[i+2])
                print ('test')
                print ()

                if tab[i-2] == '-' :
                    left = float(tab[i-1]) * -1
                    tab[i-2] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    left = float(tab[i-1])

                if tab[i+1] == '-' :
                    right = float(tab[i+2]) * -1
                    tab[i+1] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    right = float(tab[i+2])

                res = left % right
                tab[i-1] = '#'
                tab[i+2] = str(res)
                tab[i] = '#'
                
            
            print ()
            print ('^^^^^^')
            print (tab)
            print ('^^^^^^ss')
            tab = clean(tab)  
            length = len(tab)
            i = 0
        i += 1
    
   
    tab = clean(tab)
    # start with * && /
    length = len(tab)
    i = 0
    while i < length :
        # Multiplication
        if tab[i] == '*' :
            print (tab)
            
            try : 
                float(tab[i+1])
                print ()
                print ('********')
                print (tab)
                print ('********')
                print ()
                if tab[i-2] == '-' :
                    res = -1 * float(tab[i-1]) * float(tab[i+1])
                    tab[i-2] = '#'
                else :
                    res = float(tab[i-1]) * float(tab[i+1])
                tab[i-1] = '#'
                tab[i+1] = str(res)
                tab[i] = '#'
            except :
                print ()
                print (tab[i-1])
                print (tab[i])
                print (tab[i+1])
                print (tab[i+2])
                print ('test')
                print ()

                if tab[i-2] == '-' :
                    left = float(tab[i-1]) * -1
                    tab[i-2] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    left = float(tab[i-1])

                if tab[i+1] == '-' :
                    right = float(tab[i+2]) * -1
                    tab[i+1] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    right = float(tab[i+2])

                res = left * right
                tab[i-1] = '#'
                tab[i+2] = str(res)
                tab[i] = '#'
                
            
            print ()
            print ('^^^^^^')
            print (tab)
            print ('^^^^^^ss')
            tab = clean(tab)  
            length = len(tab)
            i = 0
        i += 1
    tab = clean(tab)
    length = len(tab)
    i = 0
    while i < length :
        # Devision
        if tab[i] == '/' :
            print (tab)
            
            try : 
                float(tab[i+1])
                print ()
                print ('********')
                print (tab)
                print ('********')
                print ()
                if tab[i-2] == '-' :
                    res = -1 * float(tab[i-1]) / float(tab[i+1])
                    tab[i-2] = '#'
                else :
                    res = float(tab[i-1]) / float(tab[i+1])
                tab[i-1] = '#'
                tab[i+1] = str(res)
                tab[i] = '#'
            except :
                print ()
                print (tab[i-1])
                print (tab[i])
                print (tab[i+1])
                print (tab[i+2])
                print ('test')
                print ()

                if tab[i-2] == '-' :
                    left = float(tab[i-1]) * -1
                    tab[i-2] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    left = float(tab[i-1])

                if tab[i+1] == '-' :
                    right = float(tab[i+2]) * -1
                    tab[i+1] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    right = float(tab[i+2])

                res = left / right
                tab[i-1] = '#'
                tab[i+2] = str(res)
                tab[i] = '#'
                
            
            print ()
            print ('^^^^^^')
            print (tab)
            print ('^^^^^^ss')
            tab = clean(tab)  
            length = len(tab)
            i = 0
        i += 1
        
    tab = clean(tab)
    # End with + && -
    length = len(tab)
    i = 0
    while i < length :
        # Multiplication
        # if tab[i] == '+' :
        #     print ()
        #     print ('PLUUS')
        #     print (tab[i-2])
        #     print (tab[i-1])
        #     print (tab[i+1])
        #     print ('PLUUS')
        #     print ()
        #     if tab[i-2] == '-' :
        #         res = -1 * float(tab[i-1]) + float(tab[i+1])
        #         print (res)
        #         print ('oooo')
        #     else :
        #         res = float(tab[i-1]) + float(tab[i+1])
        #     tab[i-1] = '#'
        #     tab[i+1] = str(res)
        #     tab[i] = '#'
        #     print (tab)
        #     length = len(tab)
        #     i = 0
        # i += 1
        if tab[i] == '+' :
            print (tab)
            
            try : 
                float(tab[i+1])
                print ()
                print ('********')
                print (tab)
                print ('********')
                print ()
                if tab[i-2] == '-' :
                    res = -1 * float(tab[i-1]) + float(tab[i+1])
                    tab[i-2] = '#'
                else :
                    res = float(tab[i-1]) + float(tab[i+1])
                tab[i-1] = '#'
                tab[i+1] = str(res)
                tab[i] = '#'
            except :
                print ()
                print (tab[i-1])
                print (tab[i])
                print (tab[i+1])
                print (tab[i+2])
                print ('test')
                print ()

                if tab[i-2] == '-' :
                    left = float(tab[i-1]) * -1
                    tab[i-2] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    left = float(tab[i-1])

                if tab[i+1] == '-' :
                    right = float(tab[i+2]) * -1
                    tab[i+1] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    right = float(tab[i+2])

                res = left + right
                tab[i-1] = '#'
                tab[i+2] = str(res)
                tab[i] = '#'
                
            
            print ()
            print ('^^^^^^')
            print (tab)
            print ('^^^^^^ss')
            tab = clean(tab)  
            length = len(tab)
            i = 0
        i += 1

    tab = clean(tab)  
    length = len(tab)
    i = 0
    while i < length :
        # Devision
        if tab[i] == '-' :
            print (tab)
            
            try : 
                float(tab[i+1])
                print ()
                print ('********')
                print (tab)
                print ('********')
                print ()
                if tab[i-2] == '-' :
                    res = -1 * float(tab[i-1]) - float(tab[i+1])
                    tab[i-2] = '#'
                else :
                    res = float(tab[i-1]) - float(tab[i+1])
                tab[i-1] = '#'
                tab[i+1] = str(res)
                tab[i] = '#'
            except :
                print ()
                print (tab[i-1])
                print (tab[i])
                print (tab[i+1])
                print (tab[i+2])
                print ('test')
                print ()

                if tab[i-2] == '-' :
                    left = float(tab[i-1]) * -1
                    tab[i-2] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    left = float(tab[i-1])

                if tab[i+1] == '-' :
                    right = float(tab[i+2]) * -1
                    tab[i+1] = '#'
                    #print (tab[i+2])
                    ##res = float(tab[i-1]) * float(tab[i+2]) * -1
                else :
                    right = float(tab[i+2])

                res = left - right
                tab[i-1] = '#'
                tab[i+2] = str(res)
                tab[i] = '#'
                
            
            print ()
            print ('^^^^^^')
            print (tab)
            print ('^^^^^^ss')
            tab = clean(tab)  
            length = len(tab)
            i = 0
        i += 1
    print (tab)
    return tab[-1]

    


# print(my_eval("2*3+5/5-6+4%4*2"))

def my_calc(x):
    x = x.replace(" ", "")
    result = ''
    if '(' in x :
        length = len(x)
        parenthese = 0
        i = 0
        while i < length :
            if x[i] == '(' :
                try:
                    int(x[i-1])
                    x = list(x)
                    x[i] = '*('
                    x = ''.join(x)
                    return my_calc(x)
                except :
                    sddsf = 0
                    
                open_index = i
                parenthese += 1
            elif x[i] == ')' :
                # print ('--------')
                # print (x[open_index+1: i])
                # print ('--------')
                res = my_eval(x[open_index+1: i])
                j = open_index
               
                while j <= i:
                    x = list(x)
                    x[j] = ''
                    if j == i :
                        if float(res) > 0 :
                            x[j] = '+' + str(res)
                        else :
                            x[j] = str(res)         

                    j += 1
                x = ''.join(x)
                length = len(x)
             
                parenthese -= 1

                if parenthese != 0 :
                    print (x)
                    return my_calc(x)
                else :
                    try :
                        # print ('+++++++')
                        # print (x)
                        # print ('+++++++')
                        x = my_eval(x)
                        result = str(x)
                        i = length + 1
                        length = len(str(x))
                        return result
                       
                    except :
                        i -=1
            i += 1 
       
    else :
        return result

# print(my_calc("3 + 4*(5 + 6*(7-8*(9*10) - 3 / 7) - 6*4)-3+1"))
print(my_calc("3 + 5(6+7(6+2-5)+3((2-3)+3)+2)"))
# print(my_eval("-2%-2"))