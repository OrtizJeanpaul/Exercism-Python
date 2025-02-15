def square_of_sum(number):
    if number == 0:
        return 0
    result = number + square_of_sum(number-1)

    return result**2

def sum_of_squares(number):
    if number == 0:
        return 0
    return number**2 + sum_of_squares(number-1)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number) 
