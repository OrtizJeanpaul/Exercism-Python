def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for index in lists:
        result.extend(index)

    return result

def filter(function, list1):
    result = []

    for item in list1:
        if function(item):
            append(item)

    return result

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