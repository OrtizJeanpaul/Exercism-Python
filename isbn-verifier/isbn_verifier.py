def is_valid(isbn):
    if(len(isbn) < 10):
        return False
    isbn = isbn.replace("-","")
    index = 0
    total = 0
    allowed_chars = "0123456789xX"
    while index <10:
        temp = isbn[index]
        if(allowed_chars.find(temp) != -1):
            if(temp.lower() == "x"):
                if(index == 9):
                    temp = 10
                else:
                    return False
            total += (int(temp) * (10 - index))
            index+=1
        else:
            return False
    return total % 11 == 0
    