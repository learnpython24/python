import random

def has_duplicate_birthday(birthdays):
    return len(birthdays) != len(set(birthdays))

def generate_birthdays(n):
    return [random.randint(0, 364) for _ in range(n)]

def birthday_paradox_simulation(trials=10000):
    print(f"{'People':>6} {'Probability of shared birthday':>30}")
    print("-" * 40)

    for n in range(5, 101, 5):
        count_shared = 0
        for _ in range(trials):
            birthdays  =  generate_birthdays(n)
            if has_duplicate_birthday(birthdays):
                count_shared += 1
            probability = count_shared / trials
        print(f"{n:>6} {probability:>30.4f}")

birthday_paradox_simulation()