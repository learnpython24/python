import random

def my_choice(sequence):
    if len(sequence) == 0:
        raise ValueError("Its an empty sequence")
    index = random.randrange(len(sequence))
    return sequence[index]

print(my_choice([1, 3, 5, 6]))