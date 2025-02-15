from collections.abc import Iterable as iter

def flatten(iterable):
    result = []
    temp = iterable[index]
    for index in range(len(iterable)):
        if isinstance(temp, iter) == True:
            result.extend(temp)
        else:
            if temp is not None:
                result.append(temp)
    
    result = [x for x in result if x != None]

    return result
        
