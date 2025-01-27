import math
def score(x, y):
    hypo = math.hypot(x,y)

    if 0 <= hypo <=1:
        return 10  
    
    if  hypo <= 5:
        return 5
    
    if  x <= 10:
        return 1

    return 0

