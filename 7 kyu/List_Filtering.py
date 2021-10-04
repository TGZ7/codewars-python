def filter_list(l):
    'Takes a list with numbers and strings and the strings are filtered out'      
    return [i for i in l if not isinstance(i,str)]
