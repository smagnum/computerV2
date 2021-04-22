


def mul_matrix(x) :
    x = x.replace(' ', '')
    x = x.split('*')
    print ('X :')
    print (x)
    print ()

    n1 = 0
    m1 = 0
    n2 = 0
    m2 = 0
    for chunk in x :
        chunk = chunk[1:-1]
        if chunk[0] == '[' and chunk[-1] == ']':
            var1 = chunk.split(';')
            new_var = var1[0].split(',')

            if x[0][1:-1] == chunk :
                n1 = len(var1)
                m1 = len(new_var)
            else :
                n2 = len(var1)
                m2 = len(new_var)

        else :
            print ('Bad format')

    

    # print ('N1 : ')
    # print (n1)
    # print ('M1 : ')
    # print (m1)
    # print ('N2 : ')
    # print (n2)
    # print ('M2 : ')
    # print (m2)

    if m1 == n2:
        
        var0 = x[0][1:-1]
        
        var0 = var0.split(';')
      
        var1 = x[1][1:-1]
        
        var1 = var1.split(';')
   

        val = 0
        for v0 in var0 :
           
          
            v0 = v0[1:-1]
           
            v0 = v0.split(',')
          
            for v1 in var1 :
               
                v1 = v1[1:-1]
                v1 = v1.split(',')
               
                i = 0
                
                while i < len(v1):
                    print (v0[i])
                    print (v1[i])
                    val += int(v0[i]) * int(v1[i])
                    i += 1

        print (val)
    else:
        print ('Sorry')

mul_matrix("[[2,3];[4,3]] * [[2,33];[1,3]]")

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