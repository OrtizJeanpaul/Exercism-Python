def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    counter = 0

    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            counter += 1
    
    return counter
