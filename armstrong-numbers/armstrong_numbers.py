def is_armstrong_number(number):
    if 0 <= number < 10:
        return True

    num = number

    digits = []
    while num > 0:
        digits.append(num%10)
        num //= 10

    return sum((digits**len(digits))) == number
