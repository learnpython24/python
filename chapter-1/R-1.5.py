import array

def sum_of_square(n):
    return sum(i * i for i in range(1, n))

print(sum_of_square(7))