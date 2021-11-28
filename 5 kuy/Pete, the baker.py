# Pete, the baker

# Write a function cakes(), which takes the recipe (object) and the available 
# ingredients (also an object) and returns the maximum number of cakes Pete can bake 
# (integer)

def cakes(recipe, available):
    import math
    div=[]
    # Check the division between available and recipe and take the minimum
    for i in recipe.keys():
        try:
            div.append(math.floor(available[i]/recipe[i]))
        except:
            div.append(0)
    return min(div)
