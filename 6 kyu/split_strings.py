# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the 
# missing second character of the final pair with an underscore ('_').

def solution(s):
    my_list=[]
    
    if len(s)%2==0:
        for i in range(0,len(s),2):
            my_list.append(s[i]+s[i+1])
    else:
        for i in range(0,len(s)-1,2):
            my_list.append(s[i]+s[i+1])
        my_list.append(s[-1]+'_')
        
    return my_list
