
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


    if m1 == n2:
        
        var0 = x[0][1:-1]
        
        var0 = var0.split(';')
      
        var1 = x[1][1:-1]
        
        var1 = var1.split(';')
   
        i = 0
        while i < len(var0):
            var0[i] = var0[i][1:-1]
            var0[i] = var0[i].split(',')
            i += 1
        i = 0
        while i < len(var1):
            var1[i] = var1[i][1:-1]
            var1[i] = var1[i].split(',')
            i += 1
    
        my_list = []
        val = 0
        i = 0
        while i < n1 :
            j = 0
            while j < m2 :
                k = 0
                while k < m1 :
                    val += int(var0[i][k]) * int(var1[k][j])
                    
                    if k == m1 -1:
                        my_list.append(val)
                        val = 0
                    k += 1
                j += 1
            i += 1
        
        print ('RESULT')
        print (my_list)

    else:
        print ('Sorry')

# mul_matrix("[[1,2,0];[4,3,1]] * [[5,1];[2,3];[3,4]]")

def add_matrix(x) :
    x = x.replace(' ', '')
    sous = False
    if ']-[' in x :
        sous = True
        x = x.replace(']-[', ']@[')
    
    elif ']+[' in x :
        x = x.replace(']+[', ']@[')


    x = x.replace(']+[', ']@[')
    x = x.split('@')
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
    

    print ('N1')
    print (n1)
    print ('M1')
    print (m1)
    print ('N2')
    print (n2)
    print ('M2')
    print (m2)
    print ()

    if n1 == n2 and m1 == m2:
        var0 = x[0][1:-1]
        
        var0 = var0.split(';')
      
        var1 = x[1][1:-1]
        
        var1 = var1.split(';')
        
        print ('Do operation')
        

        i = 0
        while i < len(var0):
            var0[i] = var0[i][1:-1]
            var0[i] = var0[i].split(',')
            i += 1
        i = 0
        while i < len(var1):
            var1[i] = var1[i][1:-1]
            var1[i] = var1[i].split(',')
            i += 1
        
        print (var0)
        print (var1)

        my_list = []
        val = 0
        i = 0
        while i < n1 :
            j = 0 
            while j < m1 :
                if sous == True :
                    val += int(var0[i][j]) - int(var1[i][j])
                else :
                    val += int(var0[i][j]) + int(var1[i][j])
                
                my_list.append(val)
                val = 0
                j += 1
            i += 1
        
        print (my_list)
    else :
        print ('Sorry')

#add_matrix("[[1,-2];[4,3];[1,5]] - [[5,1];[2,3];[3,4]]")

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

        result = ''
        for chunk in x :
            if chunk[0] == '[' and chunk[-1] == ']':
                res = chunk.replace('', '')
                result += ' ' + res
            else :
                print ('Bad format')
        return result       
    else :
        print ('Bad format')

    


#check_matrix("[[3,4]]")
