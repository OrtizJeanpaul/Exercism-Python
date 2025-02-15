from collections.abc import Iterable as iter

def flatten(iterable):
    result = []
    
    for index in range(len(iterable)):
        temp = iterable[index]
        if isinstance(temp, iter) == True:
            result.extend(flatten(temp))
        else:
            if temp is not None:
                result.append(temp)
    
    result = [x for x in result if x != None]

    return result
        
