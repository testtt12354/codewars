
#8kyu
def final_grade(exam, projects):
    
    if exam >= 90 or projects > 10:
        return 100
    elif exam >= 75 and projects >= 5:
        return 90
    elif exam >= 50 and projects >= 2:
        return 75
    else:
        return 0
        

#8kyu
def fake_bin(x):
    result = ""
    for i in x:
        if int(i) >= 5:
            result+='1'
        else:
            result += '0'  
    return result     

#7kyu
def sum_two_smallest_numbers(numbers):
    sort = sorted(numbers)
    
    return sort[0] + sort[1]

#7kyu
def to_jaden_case(string):
    words = string.split()
    
    capitalize = []
    
    for i in words:
        capitalize2 = i.capitalize()
        capitalize.append(capitalize2)
        
    result = ' '.join(capitalize)
        
    return result