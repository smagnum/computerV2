


def complex_number(x) :
    x = x.replace(' ', '')
    x = x.replace('-', '+-')
    x = x.split('+')

    i_list = []
    regular_list = []

    for number in x:
        if 'i' in number :
            i_list.append(number)
        else :
            regular_list.append(number)

    i_total = 0
    for number in i_list :
        if '*' in number :
            number = number.split('*')
        else :
            number = number.split('i')
        i_total += int(number[0])
    
    i_total = str(i_total) + '*i' 

    regular_total = 0
    for number in regular_list :
        if number != '':
            regular_total += int(number)

    if i_total[0] != '-' : 
        i_total = '+' + i_total

    result = str(regular_total) + str(i_total)

    return result
    
