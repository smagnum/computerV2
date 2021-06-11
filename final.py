import sys
import re
import json



#======================================================

import jsonify

from polynom import polynom
from number import numbers
from complex_number import complex_number
from Matrix import check_matrix
from calc import my_eval

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# def check_complex(x):
#     try :
#         x = x.replace('-', '+-')
#         x = x.split('+')

#         i_list = []
#         numbers = []
#         for chunk in x :
#             print (chunk)
#             if 'i' in chunk :
#                 i_list.append(chunk)
#                 if len(i_list) > 1:
#                     print (i_list)
#             else :
#                 numbers.append(chunk)
        
        

#         print ('The try : ')
#         print (x)

#         return x
#     except : 
#         print ('The except : ')
#         return x


elms = {}
regex = re.compile('[a-z]|[A-Z]')

while True :
    args = input('>>> ')
    args = args.replace(' ', '')
    
    checker = regex.findall(args)
    if '=' in args :
        test = args
        args = args.split('=')

        if len(args)  == 2 :
            checker = regex.findall(args[0])

            if '?' in args[1] :
               
                equation = list(args[0])
                print (equation)
                for eq in equation :
                    if eq in elms :
                        equation[equation.index(eq)] = str(elms[eq])
                        print (equation)

                equation = ''.join(equation)
                value = my_eval(equation)
                print (value)
            elif args[0] != '' and args[1] != '' and len(checker) != 0:             
                var = args[0]
                if var != 'i':
                    try :
                        if '(' in args[0]:
                            value = polynom(args[1] + ' = 0')
                            print ('+++++++++++++++++polynome++++++++++++++')
                            print (value['reduce_form'])
                            elms[var] = value['reduce_form']
                            print ('+++++++++++++++++polynome++++++++++++++')
                        elif 'i' in args[1] :
                            try : 
                                value = complex_number(args[1])
                                print (value)
                                elms[var] = value
                            except :
                                print ('Bad format')
                        elif '[' in args[1] :
                            value = check_matrix(args[1])
                            elms[var] = value
                            value = value.split(" ")
                            i = len(value)
                            j = 1
                            while j < i : 
                                print (value[j])
                                j += 1
                        else :
                            value = numbers(args[1], elms)
                            elms[var] = value
                            print (value)
                        #print (value)
                    except e:
                        print (e)
                        print ('sBad format')
                else :
                    print ("You can't reserve i")
                
            else :
                print ('qBad format')
        else :
            print ('Bad format')

    elif args in elms :
        print (elms[args])
    elif len(checker) == 0 :
        try :
            value = eval(args)
            print (value)
        except :
            print ('Bad format')
    elif args == 'quit':
        sys.exit()
    else :
        print (0)



#   rational numbers
#   complexe numbers
#   matrice
#   functions
#   switch computerV1 to function and imported


