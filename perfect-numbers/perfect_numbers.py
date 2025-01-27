from multiprocessing import Value


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    factor_sum = sum(factors(number))

    if factor_sum == number:
        return "perfect"

    return "abundant" if number < factor_sum else "deficient"

def factors(number):
    half = number // 2
    factor_list = []
    for index in range(1,half+1):
        if number % index == 0:
            factor_list.append(index)
    
    return factor_list