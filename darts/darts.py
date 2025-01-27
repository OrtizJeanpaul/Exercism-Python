def score(x, y):
    if 0 <= x <=1  and 0 <= y <= 1:
        return 10
    
    if 2 <= x <= 5 and 2 <= y <= 5:
        return 5
    
    if 6 <= x <= 10 and 6 <= y <= 10:
        return 1

    return 0