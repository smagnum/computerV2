import sys
import re
import json



#======================================================

import jsonify

from polynom import polynom



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
            if args[0] != '' and args[1] != '' and len(checker) != 0:             
                var = args[0]
                if var != 'i':
                    try :
                        if 'x' in test:
                            value = polynom(test)
                            print ('+++++++++++++++++polynome++++++++++++++')
                            print (value)
                            print ('+++++++++++++++++polynome++++++++++++++')
                        else :
                            value = numbers(args[1])
                            elms[var] = value

                        #print (value)
                    except e:
                        print (e)
                        print ('sBad format')
                else :
                    print ("You can't reserve i")
                
            else :
                print ('Bad format')
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


