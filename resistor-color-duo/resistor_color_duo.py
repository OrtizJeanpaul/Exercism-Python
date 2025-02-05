def value(colors):
    COLOR_ARRAY = ["black", "brown", "red", "orange", "yellow", "green", "blue","violet", "grey","white"]

    res = ""
    for index in range(2):
        res += COLOR_ARRAY.index(colors[index])
    
    return int(res)
