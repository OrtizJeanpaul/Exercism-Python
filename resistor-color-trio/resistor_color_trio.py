import math
def label(colors):
    COLOR_ARRAY = ["black", "brown", "red", "orange", "yellow", "green", "blue","violet", "grey","white"]

    res = 10*COLOR_ARRAY.index(colors[0]) + COLOR_ARRAY.index(colors[1])
    num_of_zeros = math.pow(10, COLOR_ARRAY.index(colors[2]))


    res = res * num_of_zeros
    prefix = " "


    if res % 1000000000 != res:
        res = res / 1000000000
        prefix = " giga"
    elif res % 1000000 != res:
        res = res / 1000000
        prefix = " mega"
    elif res % 1000 != res:
        res = res / 1000
        prefix = " kilo"
    return str(int(res)) + prefix + "ohms"