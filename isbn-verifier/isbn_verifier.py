def is_valid(isbn):
    isbn = isbn.replace("-","")

    index = 0
    total = 0
    while index <10:
        temp = isbn[index]
        if(temp == "x"):
            temp = 10
        total += (int(temp) * (10 - index))
    return total % 11 == 0