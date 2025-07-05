import array

def sum_of_odd_square(n):
    if n <= 0:
        raise ValueError("n must be a postive number")
    return sum(i * i for i in range(1, n) if i % 2 == 1)

print(sum_of_odd_square(7))
