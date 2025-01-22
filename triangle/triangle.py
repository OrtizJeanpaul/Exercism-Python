def is_valid_triangle(sides):
    a,b,c = sides
    return a+b+c >=3 and (a+b >=c and b+c >=a and a+c >=b)

def equilateral(sides):
    a,b,c = sides

    return a == b == c and is_valid_triangle(sides)


def isosceles(sides):
    return len(set(sides)) < 3 and is_valid_triangle(sides)


def scalene(sides):
    return len(set(sides)) == 3 and is_valid_triangle(sides)


