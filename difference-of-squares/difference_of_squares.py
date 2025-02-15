def square_of_sum(number):
    return sum(number)**2 if len(number) > 1 else number**2


def sum_of_squares(number):

    return sum(number**2) if len(number) > 1 else number**2


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number) 
