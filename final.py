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
            else :
                str_list.append(val[i]) 
        
        i += 1
    # print (str_list)
    # print (myStr)
    return str_list

# get_string('14so243u23ha4il')

def search_string(str_list, myString):
    if myString in str_list :
        return str_list[myString]



def numbers(x) :

    if 'i' in x:
        if '-' in x:
            x = x.replace('-', '+-')
        x = x.split('+')
      
        val = ''
        i = 0
        while i < len(x) :
            if 'i' in x[i] :
                
                new = x[i]
                x.remove(x[i])
                x.append(new)
            i +=1
        
        for chunk in x :
            val += chunk
            if chunk != x[-1]:
                val += '+'
    
        return val
        
    else :
        try :
            value = int (x)
        except :
            try :
                value = eval(x)
            except :
                value = ''
                str_list = get_string(x)
            
                for myStr in str_list:
                    result = search_string(elms, myStr)
                    
                    if result != None :
                        value += str(result)
                    else :
                        value += myStr
                
                value = eval(value)

        return value


elms = {}
regex = re.compile('[a-z]|[A-Z]')

while True :
    args = input('>>> ')
    args = args.replace(' ', '')
    checker = regex.findall(args)
    if '=' in args :
        
        args = args.split('=')

        if len(args)  == 2 :
            checker = regex.findall(args[0])
            if args[0] != '' and args[1] != '' and len(checker) != 0:             
                var = args[0]
                if var != 'i':
                    try :
                        value = numbers(args[1])
                        elms[var] = value
                        print (value)
                    except e:
                        print (e)
                        print ('Bad format')
                else :
                    print ("You can't reserve i")
                
            else :
                print ('Bad format')
        else :
            print ('Bad format')

    elif args in elms :
        print (elms[args])
    elif checker != 0 :
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
#   switch computerV1 to function and imported


