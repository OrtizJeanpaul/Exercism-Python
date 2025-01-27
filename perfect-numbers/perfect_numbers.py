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
        return "Perfect"

    return "Abundant" if number > factor_sum else "Deficient"

def factors(number):
    half = number // 2
    factor_list = []
    for index in range(1,half):
        if number % index:
            factor_list.append(index)
    
    return factor_list