import array

def distinct_sequence(sequence):
    checked_sequence = sequence
    for a in sequence:
        new_sequence = []
        exit = 0
        for c in checked_sequence:
            if c == a and exit < 1:
                exit += 1
                new_sequence.append(c)
            elif c != a:
                new_sequence.append(c)
        checked_sequence = new_sequence
    return len(checked_sequence) == len(sequence)

def distinct_use_set(sequence):
    return len(sequence) == len(set(sequence))

print(distinct_sequence([1, 2, 2, 3, 5]))
print(distinct_use_set([1, 2, 2, 3, 5]))