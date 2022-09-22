def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError("Strands must be of equal length.")
    distance = 0

    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            distance += 1
        
    return distance

        

