def append(list1, list2):
    if not list1 or not list2:
        return list2 if not list1 else list1
        
    for item in enumerate(list2):
        list1.__add__(item[1])

    return list1

def concat(lists):
    result = []
    for sList in enumerate(lists):
        result.extend(sList)

    return result

def filter(function, list):
    return

def length(list):
    i = 0
    for index in list:
        i = index

    return i+1


def map(function, list):
    return

def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    result = []
    index = length(list) - 1
    
    while index >= 0:
        append(result, [list[index]])
        index-=1
    
    return result