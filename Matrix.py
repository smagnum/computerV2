


def mul_matrix(x) :
    x = x.replace(' ', '')
    x = x.split('*')
    print ('X :')
    print (x)
    print ()

    

    n1 = 0
    for chunk in x :
        chunk = chunk[1:-1]
        if chunk[0] == '[' and chunk[-1] == ']':
            
            i = 1
            for char in chunk :
                if char == ';':
                    i += 1

            if x[0][1:-1] == chunk :
                n1 = i 
            else :
                m2 = i

        else :
            print ('Bad format')

    print ('N1 : ')
    print (n1)
    print ('M2 : ')
    print (m2)

    if n1 == m2:
        print ('Do equation')
    else:
        print ('Sorry')

mul_matrix("[[2,3];[4,3];[5,4];[1,2]] * [[2,33];[1,3]]")

def check_matrix(x) :
    x = x.replace(' ', '')
    if '*' in x :
        x = x.split('*')

        n1 = 0
        for chunk in x :
            chunk = chunk[1:-1]
            if chunk[0] == '[' and chunk[-1] == ']':
                print ('valid')
                print (chunk)

                i = 1
                for char in chunk :
                    if char == ';':
                        i += 1

                n1 = i
    
            else :
                print ('Bad format')

    elif x[0] == '[' and x[-1] == ']':
        x = x[1:-1]
        x = x.split(';')

        for chunk in x :
            if chunk[0] == '[' and chunk[-1] == ']':
                print (chunk.replace('', ''))
            else :
                print ('Bad format')
            
    else :
        print ('Bad format')

    


# check_matrix("[[2,3];[4,3];[5,4];[1,2]] * [[2,33]]")