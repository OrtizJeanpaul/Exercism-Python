import math
def label(colors):
    COLOR_ARRAY = ["black", "brown", "red", "orange", "yellow", "green", "blue","violet", "grey","white"]

    res = ""
    num_of_zeros = math.pow(10, COLOR_ARRAY.index(colors[2]))
    for index in range(2):
        res += str(COLOR_ARRAY.index(colors[index]))

    res = int(res) * num_of_zeros

    return str(res) + " ohms"