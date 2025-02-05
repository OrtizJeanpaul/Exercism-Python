def resistor_label(colors):
    TOLERANCE_DICT =  {"Grey" : "0.05%", "Violet" : "0.1%",
                       "Blue" : "0.25%","Green" : "0.5%",
                       "Brown" : "1%","Red" : "2%",
                       "Gold" : "5%","Silver" : "10%"}
    
    COLOR_ARRAY = ["black", "brown", "red", 
                   "orange", "yellow", "green", 
                   "blue","violet", "grey","white"]

    res = 10*COLOR_ARRAY.index(colors[0]) + COLOR_ARRAY.index(colors[1])
    num_of_zeros = 10**COLOR_ARRAY.index(colors[2])
    tolerance = f"± {TOLERANCE_DICT[colors[3]]}"

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

    return str(int(res)) + prefix + "ohms" + tolerance
