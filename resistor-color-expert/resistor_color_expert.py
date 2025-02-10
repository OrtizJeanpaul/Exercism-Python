
def resistor_label(colors):
    TOLERANCE_DICT =  {"grey" : "0.05%", "violet" : "0.1%",
                       "blue" : "0.25%","green" : "0.5%",
                       "brown" : "1%","red" : "2%",
                       "gold" : "5%","silver" : "10%"}
    
    COLOR_ARRAY = ["black", "brown", "red", 
                   "orange", "yellow", "green", 
                   "blue","violet", "grey","white"]
    res = ""
    if len(colors) < 3:
        return "0 ohms"
    for index in range(len(colors) - 2):
        res += str(COLOR_ARRAY.index(colors[index]))
        
    res = int(res)
    num_of_zeros = 10**COLOR_ARRAY.index(colors[-2])
    tolerance = f"±{TOLERANCE_DICT[colors[-1]]}"

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

    return "{}".format(res) + prefix + "ohms " + tolerance
