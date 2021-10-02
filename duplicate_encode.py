# Duplicate Encoder
# The goal is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    
    from collections import Counter # Import the right module
    
    low=word.lower() # All letters lowercase 
    dic=Counter(low) # Make a dict with count of each character
    final=""         # Make an empty string
    

    return final=final.join([ final+"(" if dic[i]==1 else final+")" for i in low])
    
print(final)
