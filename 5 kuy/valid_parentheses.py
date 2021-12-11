def valid_parentheses(string):
    '''
    Function that takes a string of parentheses, and determines 
    if the order of the parentheses is valid. The function return true 
    if the string is valid, and false if it's invalid.
    
    My approach is: you run through the string and you can find any number of
    '(' and still be valid (they may close later), but if you find a high number of
    ')', you know in that moment that the string is invalid. You only have to check
    at the end if the number of each character is equal and you're done.
    '''
    
    a=0
        
    for i in string:
        if i=='(':
            a+=1
        if i==')':
            if a<1:
                return False
            else:
                a-=1
    if a==0:
        return True
    else:
        return False
