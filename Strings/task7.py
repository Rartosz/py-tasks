
def not_poor(str1):
    
    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot > 0 and spoor > 0:
        
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        
        return str1
print(not_poor('The lyrics is not that poor!'))        
