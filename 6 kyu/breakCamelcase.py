'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""                   
'''

def solution(s):
    ss=s    # new sentence
    a=0     # we will add 1 to the index for each uppercase found, in case we find another
    for j,i in enumerate(s):
        j+=a # If we find an uppercase, we add 1 to j because the space we add
        if i != i.lower():
            ss=ss[:j]+' '+ss[j:]
            a+=1
    return ss
