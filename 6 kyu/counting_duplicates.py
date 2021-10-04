def duplicate_count(text):
    from collections import Counter    # Importing the Counter function
    n=0
    for i in list(Counter(text.lower()).values()):  # Through the count of each lowercased character
        if i>1:
            n+=1                                    # If any character is more that once, n adds 1
    return n
