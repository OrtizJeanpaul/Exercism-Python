def score(x, y):
    if 0 <= x <=1  and 0 <= y <= 1:
        return 10
    
    if  x <= 5 and  y <= 5:
        return 5
    
    if  x <= 10 and  y <= 10:
        return 1

    return 0