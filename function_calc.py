import re


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


def my_list(tab) :
    tab = list(tab)
    length = len(tab)
    i = 0
    num = ''
    res = []
    while i < length :
        try :
            int (tab[i])
            is_number = 1
        except :
            is_number = 0

        if is_number == 1 :
           num += str(tab[i])
           if i +1 == length :
               res.append(num)
        else :
            if tab[i] == 'y' :
                num += str(tab[i])
            else :
                res.append(num)
                num = ''
                # num += tab[i]
                res.append(tab[i])
            # num = ''
        i += 1
    
    res = clean(res)

    return (res)

# print (my_list("y+1-11"))


def simpli_A(tab, number) :
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
           
            num = ''
        except :
            if chunk == '+' or chunk == '-':
                num = str(num) + str(chunk)
            
                tab[tab.index(chunk)] = ''
            else :
            
                try :
                    
                    res.append(int(number) * int(chunk))
                except :
                   
                    test = chunk.split('y')
                
                  
                    for kk in test :
                        try :
                            sdf = 1
                            int(kk)
                
                            k = int(kk) * int(number)
                        
                            k = str(k) + 'y'
                            res.append(k)
                        except :
                            sdf = 0
                    
                    if sdf == 0 :
                        # if len(chunk) == 1 :
                        print ('hnaa')
                        print ('----')
                        print (chunk)
                        print (number)
                        print ('-----')
                        res.append(str(chunk)+ str(number))
                        print (res)

    print (res)
    for test in res :
        try :
            testo = test.split('y')
            
            if testo[1] != '' and testo[0] != '':
                res[res.index(test)] = ''
        except : 
            print ('ok')
    print (res)
    return res

# tab = ['2y', -2]
# print (simpli_A(tab, 4))

def simpli_B(tab) :
    tab = my_list(tab)
   
    res = []
    num = ''
    for chunk in tab :
  
        try :
            if 'y' in chunk :
                
                num += chunk
                
                if '-' in num :
                    num = num
                elif '+' in num :
                    num = num.replace('+', '')
                tab[tab.index(chunk)] = num
             
                res.append(num)
                num = ''
            else :
                
                int(chunk)
                num += chunk
               
                if '-' in num :
                    num = int(num)
                elif '+' in num :
                    num = num.replace('+', '')
                
                tab[tab.index(chunk)] = num
                res.append(int(num))
                num = ''
        except :
            if chunk == '+' or chunk == '-':
                num += str(chunk)
                tab[tab.index(chunk)] = ''
                
            else :
                res.append(chunk)
    return res
# popo = ['-', '2y', '+', '3y', '-', '2']
# print (simpli_B(popo))

def multiple (tab, number) :

    # try :
    #     int(number)
    #     print ('ok')
    # except :
    #     print ('Do boucle ')
    # nums = list(number)

    # print (nums)
    
    nums = simpli_B(number)

  
    new_tab = simpli_B(tab)
  


    glob_res = ''
    for nu in nums :
        
        res = simpli_A(new_tab, nu)
    
        for r in res :
            glob_res += '+' + str(r) 
        # glob_res.append(res)

   
    # print (glob_res)
    # glob_res = glob_res.replace('+-', '-')
    # print (glob_res)
    while '+-' in glob_res : 
        glob_res = glob_res.replace('+-', '-')
    


 
    return glob_res



# print(multiple("y+2", "4"))
   
  
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



# print(multiple("-1-5+6", "y+11-2"))

def reduce_parenthese (paranthese_number, x) :
    param = my_list(paranthese_number)
 
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
        
            res = multiple(per, param[open_index - 1])
         
            
            param[open_index -1:i ] = '#'
            param[open_index] = res
            
            i = 0
            length = len(param)
          

            if '(' in param :

                reduce_parenthese (param, x)


            # try :
            #     float(param[open_index - 1])
                
            #     if x in param[open_index:i+1] :
            #         print ('yesy')
            #         num += param[open_index - 1] + x

            # except :
            #     num += param[open_index - 1] + x
            
            parenthese -= 1

        
        # print (param[i])
        i += 1
    # print (num)

# reduce_parenthese("5(3+22(y+1))", 'y')
# print (simpli_B("3+22"))


def fix (tab) :
    res = ''
    for chunk in tab :
        res += chunk
    res = my_list(res)
    return res

# print (my_list('2y+1'))
    

def reduce_parenthese2 (parenthese_number, x) :
   
    if '(' in parenthese_number :
        param = my_list(parenthese_number)
      
        # print ()
        # print ('here tha param **************')
        # print (param)
        # print ('here tha param **************')
        # print()
 
        length = len(param)
        i = 0
        parenthese = 0
        num = ''
        while i < length :
            if param[i] =='(' :
                parenthese += 1
                open_index = i
            elif param[i] ==')' :
                per = param[open_index + 1: i]
    

                try :
                   
                    int(param[open_index - 1])
                
                    number_to_pass = param[open_index - 1]
                    if param[open_index - 2] == '-' :
                        number_to_pass = int(param[open_index - 1]) * -1
                    resultat = multiple (per, str(number_to_pass))
                
                
                    resultat =  my_list(resultat)
                 
                    param[open_index : i + 1] = resultat
                    param[open_index - 1] = ''

                    return reduce_parenthese2 (param , x)
                
            
                except e:
                    print ('is not number')
                   
        
            
            i += 1
    else :
        res = ''
        for chunk in parenthese_number :
            res += chunk
        
        res = res.replace('++', '+')
        res = res.replace('-+', '+')
        res = res.replace('--', '-')
        res = res.replace('+-', '+')
        
        return res
    

# print(reduce_parenthese2 ("2(2y+3)", 'y'))
# print(reduce_parenthese2 ("4(y+2)", 'y'))

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
            if i == length - 1 :
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

    


    for t in tab :
        if '(' in t :
            res = reduce_parenthese2(t, x)
            tab[tab.index(t)] = res
     

    return tab


print (function_calc("3-2(-2y+3y-2--2)- 2", 'y'))
# print (function_calc("3 + 4(y + 2)", 'y'))


