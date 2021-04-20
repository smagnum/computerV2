import sys
import re

def get_string(val):
    str_list = []
    regex = re.compile('[a-z]|[A-Z]')

    keep = False
    i = 0
    myStr = ''
    while i < len(val):        

        results = regex.findall(val[i])
        if len(results) != 0:
            myStr += val[i]
            if len(myStr) > 1:
                str_list[-1] = myStr
            else :
                str_list.append(myStr)
      
        else :
            if val[i] != val[-1]:
                check = regex.findall(val[i+1])
                if check != 0 :
                    myStr = ''
                    keep = True
                str_list.append(val[i])
        
        i += 1
    # print (str_list)
    # print (myStr)
    return str_list

# get_string('14so243u23ha4il')

def search_string(str_list, myString):
    if myStr in str_list :
        return str_list[myStr]


elms = {}

while True :
    args = input('> ')
    args = args.replace(' ', '')
    if '=' in args :
        
        args = args.split('=')

        if len(args)  == 2 :
            if args[0] != '' and args[1] != '':
                try :
                    var = args[0]
                    try:
                        int(args[1])
                    except:
                        args[1] = eval(args[1])
                        elms[var] = args[1]
                        print (elms[var])
                    
                except :
                    var = args[0]
                    val = ''
                    str_list = get_string(args[1])
                    for myStr in str_list:
                        
                        result = search_string(elms, myStr)
                        if result != None :
                            val += str(result)
                        else :
                            val += myStr

                    elms[var] = eval(val)
                    print ('val 1')
                    print (elms[var])
                    print (elms)

                    
                try :
                    
                    val = eval(args[1])
                    elms[var] = val
                    print ('val 2')
                    print (val)
                except :
                    sdg = 0
                    # val = ''
                    # str_list = get_string(args[1])
                    # print ('get string')
                    # print (str_list)
                    # print (elms)
                    # for myStr in str_list:
                        
                    #     result = search_string(elms, myStr)
                    #     if result != None :
                    #         val += str(result)
                    #     else :
                    #         val += myStr

                    # elms[var] = eval(val)
                    # print ('val 3')
                    # print (elms[var])

            else :
                print ('Bad format')
        else :
            print ('Bad format')


    elif args in elms :
        print (elms[args])

    elif args == 'quit':
        sys.exit()
    else :
        print (0)