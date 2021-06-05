import sys
import json
import jsonify

# Check duplicated item
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

# Sqrt function
def Square(n, i, j): 
  
    mid = (i + j) / 2; 
    mul = mid * mid; 
 
    if ((mul == n) or (abs(mul - n) < 0.00000000001)): 
        return mid; 
    elif (mul < n): 
        return Square(n, mid, j); 
    else: 
        return Square(n, i, mid); 
  
# Sqrt function
def findSqrt(n): 
    i = 1; 

    found = False; 
    while (found == False): 
  
      
        if (i * i == n): 
            return i; 
            found = True; 
          
        elif (i * i > n): 
              
            res = Square(n, i - 1, i); 
            res = round(res, 6)
            return res
            
            found = True
        i += 1; 
  

# More than one argument

def polynom(x):
    if 5 == 3 :
        results = {
            'msg' : 'Bad format',
            'code' : 0
        }
            
        return json.dumps(results)

    # 1 Argument
    else :
        params = str(x)

        # Separate param1 & param2
        try :
            params = params.replace('-', '+-')
            params = params.split('=')

            if len(params)> 2 :
                return json.dumps(code = 0)

            param1 = params[0].replace(' ', '')
            param2 = params[1].replace(' ', '')
        
        except :
            results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
            return json.dumps(results)

        # Check first characters\
        if param1[0] == '+' and param1[1] == '-' :
            param1 = param1[1:]

        if param2[0] == '+' and param2[1] == '-' :
            param2 = param2[1:]

        param1 = param1.split('+')
        param2 = param2.split('+')

        print (param1)
        print (param2)

        len1 = len(param1)
        len2 = len(param2)

        # Separate puiss1 & puiss2 // var1 & var2
        puiss1 = []
        puiss2 = []

        var1 = []
        var2 = []

        try :
            i = 0
            while i < len1:
                x = param1[i].replace(' ', '')

                if x[0].upper() == 'X':
                    x = '1*' + x
                    
                elif x[0] == '-' and x[1].upper() == 'X':
                    x = '-1*' + x[1:]
                if '*' in x :
                    x = x.split('*')

                    if len(x) > 2 :
                        print ('Bad format')
                        df = 0
                        sys.exit()

                    if x[1][-1] == 'X' or x[1][-1] == 'x':
                        x[1] = x[1] + '^1'
                    var1.append(x[0]) 
                    puiss1.append(x[1].upper())
                else :
                    var1.append(x)
                    puiss1.append('X^0')
                i += 1

            j = 0
            while j < len2:
                x = param2[j].replace(' ', '')

                if x[0].upper() == 'X':
        
                    x = '1*' + x
                elif x[0] == '-' and x[1].upper() == 'X':
            
                    x = '-1*' + x[1:]
                if '*' in x :
                    x = x.split('*')
                    if x[1][-1] == 'X' or x[1][-1] == 'x':
                        x[1] = x[1] + '^1'
                

                    var2.append(x[0])
                    puiss2.append(x[1].upper())
                else :
                    var2.append(x)
                    puiss2.append('X^0')
                j += 1
        except :
            if not 'df' in globals():
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)



        # Check vars and puiss :
        for var in var1 :
            try :
                float(var)
            except :
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)

        for var in var1 :
            try :
                float(var)
            except :
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)

        for puiss in puiss1 :
            if puiss[0] != 'X' :
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)

            if puiss[1] != '^' :
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)

            try :
                float(puiss[2])
            except :
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)
            
        for puiss in puiss2 :
            if puiss[0] != 'X' :
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)

            if puiss[1] != '^' :
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)

            try :
                float(puiss[2])
            except :
                results = {
                    'msg' : 'Bad format',
                    'code' : 0
                }
            
                return json.dumps(results)

        # Check duplicated Puiss
        try :
            j = 0
            while j < len(puiss1):
                dup = duplicates(puiss1, puiss1[j])
                if len(dup) > 1 :
                    i = 1
                    while i < len(dup):
                        var1[dup[0]] = float(var1[dup[0]]) + float(var1[dup[i]])
                        var1[dup[0]] = round(var1[dup[0]], 6)
                        i += 1

                    i = len(dup) - 1
                    while i >= 1:
                        del var1[dup[i]]
                        del puiss1[dup[i]]
                        
                        i -=1 
            
                j +=1
        except :
            results = {
                'msg' : 'Bad format',
                'code' : 0
            }
            
            return json.dumps(results)


        print (var1)
        print (puiss1)
        print (var2)
        print (puiss2)
        try :
            j = 0
            while j < len(puiss2):
                dup = duplicates(puiss2, puiss2[j])
                if len(dup) > 1 :
                    i = 1
                    while i < len(dup):
                        var2[dup[0]] = float(var2[dup[0]]) + float(var2[dup[i]])
                        var2[dup[0]] = round(var2[dup[0]], 6)
                        i += 1


                    i = len(dup) - 1
                    while i >= 1:
                        del var2[dup[i]]
                        del puiss2[dup[i]]
                        
                        i -=1 
                j +=1
        except :
            results = {
                'msg' : 'Bad format',
                'code' : 0
            }
            
            return json.dumps(results)

        # Switch var2 to var1
        try :
            len1 = len(puiss1)
            len2 = len(puiss2)
            exist = []
            k = 0
            while k < len1:
                u = 0
                while u < len2:
                    if puiss1[k] == puiss2[u] :
            
                        var1[k] = float(var1[k]) - float(var2[u])
                        exist.append(puiss2[u])
                    u += 1

                k += 1
        except :
            results = {
                'msg' : 'Bad format',
                'code' : 0
            }
            
            return json.dumps(results)



        try :
    
            diff = set(exist) ^ set(puiss2)
        
            for di in diff :
                i = 0 
                while i < len(puiss2):
                    if di == puiss2[i] :
            
                        puiss1.append(di)
                        var1.append(float(var2[i]) * -1)
                    i += 1
        except:
            results = {
                'msg' : 'Bad format',
                'code' : 0
            }
            
            return json.dumps(results)


        
        # Add puissance to vaiables
        try :

            len_res = len(var1)
        
            t = 0
            while t < len_res :
                var1[t] = str(var1[t]) + '*' + puiss1[t]
                t += 1




            i = 0
            while i < len(var1):
                var1[i].split('*')

                if len(var1) == 1 :
                    degree = var1[i][-1]
                try :
                    if float(var1[i][:var1[i].index("*")]) == 0 :
                        var1.remove(var1[i])
                except e:
                    askdjf= 0
                i+= 1

            
            # Order by degree
            oss = '^'
            new = sorted(var1, key=lambda x: float(x[x.index(oss) + len(oss):]))
    
            variables = []

            for n in new:
                variables.append(n)

            if len(variables) == 0 :
                msg = 'All real numbers is a solution'
            
            print (variables)
            
        except :
            results = {
                'msg' : 'Bad format',
                'code' : 0
            }
            
            return json.dumps(results)
    

        # The reduce form
        try :
            i = 0
            while i < len(new) :
                if 'X^0' in new[i] :
                    new[i] = new[i].split('*')
                    new[i] = new[i][0]

                if 'X^1' in new[i] :
                    new[i] = new[i].replace('^1', '')

                i += 1

            reduce_form = 'Reduce form : '
            i = 0
            if len(new) != 0 :
                while i < len(new):
                    if i != len(new) - 1:
                        if new[i + 1][0]  == '-':
                            reduce_form += new[i] + ' - '
                            new[i + 1] = new[i + 1][1:]
                        else :
                            reduce_form += new[i] + ' + '
                    else :
                        reduce_form += new[i]
                    i += 1
                
            else :
                reduce_form += '0*X^0'

            reduce_form += ' = 0'
        

        
        except :
            results = {
                'msg' : 'Bad format',
                'code' : 0
            }
            
            return json.dumps(results)

        

        # Get degree and abc
        try :

            if 'degree' in globals() :
                degree_form = 'Polynomial degree: ' + str(degree)
            
            else :
                degree = variables[-1].split('^')
                degree = degree[1]
                degree_form = 'Polynomial degree: ' + str(degree)
            
        
            i = 0
        
            while i < len(variables):
                if variables[i][-1] == '0' :
                    c = variables[i].split('*')
                    c = float(c[0])

                if variables[i][-1] == '1' :
                    b = variables[i].split('*')
                    b = float(b[0])
            
                if variables[i][-1] == '2' :
                    a = variables[i].split('*')
                    a = float(a[0])
                i += 1
            
            
                

        except :
            results = {
                'msg' : 'Bad format',
                'code' : 0
            }
            
            return json.dumps(results)

        
        print (b)
        print (c)
        # Some math
        Q = False
        try :
            if int(degree) > 2 :
                # print (reduce_form)
                # print (degree_form)
                #print ("The polynomial degree is strictly greater than 2, I can't solve.")
                results = {
                    'msg' : "The polynomial degree is strictly greater than 2, I can't solve."
                }
                
                return json.dumps(results)
                Q = True
            

            if Q != True :
                # if 'a' not in globals():
                #     print ('oui')
                #     a = 0

                # if 'b' not in globals():
                #     print ('non')
                #     b = 0

                # if 'c' not in globals():
                #     c = 0
                

                try :
                    check_var = a
                except :
                    a = 0
                
                try :
                    check_var = b
                except :
                    b = 0

                try :
                    check_var = c
                except :
                    c = 0

                
                if a == 0 and b == 0 and c == 0:
                    # print (reduce_form)
                    # print (degree_form)
                    # print ("All real numbers is a solution")
                    results = {
                        'msg' : "All real numbers is a solution"
                    }
                    
                    return json.dumps(results)

                elif a == 0 and b == 0 and c != 0:
                    # print (degree_form)
                    # print ("There is no solution")
                    results = {
                        'msg' : "There is no solution"
                    }
                    
                    return json.dumps(results)

                elif a == 0:
                    # print (reduce_form)
                    # print (degree_form)
                    # print ("The solution is :")
                    results = {
                        'sol' : round(-c/b, 6),
                        'msg' : "The solution is :"
                    }
                    
                    return json.dumps(results)

                else:

                    delt = (b*b) - (4*a*c)

            
                    
                    if delt > 0:
                        # print (reduce_form)
                        # print (degree_form)
                        # print("Discriminant is strictly positive, the two solutions are: ") 
                        results = {
                            'sol1' : (-b+findSqrt(delt))/(2*a),
                            'sol2' : (-b-findSqrt(delt))/(2*a),
                            'sol1' : round(sol1, 6),
                            'sol2' : round(sol2, 6), 

                            'msg' : "Discriminant is strictly positive, the two solutions are: "
                        }
                        
                        return json.dumps(results)

                    elif delt == 0:
                        # print (reduce_form)
                        # print (degree_form)
                        # print ("The only solution is : ")
                        results = {
                            'sol' : round((-b)/(2*a), 6),
                            'msg' : "The only solution is :  "
                        }
                        
                        return json.dumps(results)

                    elif delt < 0:
                        # print (reduce_form)
                        # print (degree_form)
                        # print ("Discriminant is strictly negative, the two solutions are: ")
                        results = {
                            'sol1' : str(round(-b / (2*a), 6)) + " + i * " + str(round(findSqrt(-delt)/(2*a), 6)),
                            'sol2' : str(round(-b / (2*a), 6)) + " - i * " + str(round(findSqrt(-delt)/(2*a), 6)),
                            'msg' : "Discriminant is strictly negative, the two solutions are: "
                        
                        }
                        return json.dumps(results)

        except :
            results = {
                'msg' : 'Bad format',
                'code' : 0
            }
            
            return json.dumps(results)



equation = "2*x^5 + 4*x^2 - 5*x + 4 = 0"
print (polynom(equation))


# def test():
#     restults = {
#         'test' : 'hada test',
#         'name' : 'Souhail'
#     }
#     return json.dumps(restults)

# print (test())