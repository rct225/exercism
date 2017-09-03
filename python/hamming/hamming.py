def distance(astrand, bstrand):
    if len(astrand) != len(bstrand):
        raise ValueError

    hamming_distance = 0

    for a,b in zip(astrand, bstrand):
        if a != b:
            hamming_distance += 1

    return hamming_distance
