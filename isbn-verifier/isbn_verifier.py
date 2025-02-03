def is_valid(isbn):
    isbn = isbn.replace("-","")

    index = 0
    total = 0
    while index <10:
        temp = isbn[index]
        if(temp.lower() == "x"):
            temp = 10
        total += (int(temp) * (10 - index))
        index+=1
    return total % 11 == 0