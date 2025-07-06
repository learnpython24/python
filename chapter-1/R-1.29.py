from itertools import permutations

def all_possible_strings():
    chars = ['c', 'a', 't', 'd', 'o', 'g']
    all_perms = permutations(chars)
    # print(sum(1 for _ in all_perms))
    for p in all_perms:
        print(''.join(p))

all_possible_strings()